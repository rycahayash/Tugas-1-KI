from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    # kalau ada kolom lain yang wajib, harus ditambahin ke sini
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        
        # tambahkan user
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username                = models.CharField(max_length=30, unique=True)
    is_superuser            = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    date_joined             = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_staff                = models.BooleanField(default=False)
    is_admin                = models.BooleanField(default=False)

    objects = MyAccountManager()

    # setting kolom apa yang dijadikan login
    USERNAME_FIELD = 'email'

    # kolom yang wajib diisi
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True