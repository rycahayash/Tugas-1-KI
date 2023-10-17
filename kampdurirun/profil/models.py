import os
from django.db import models
from django.utils import timezone
from user.models import User

class Profil(models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('l', 'Laki-Laki'),
        ('p', 'Perempuan'),
    )

    informasi_kesehatan = models.CharField(max_length=100)
    tinggi_badan = models.PositiveIntegerField()
    berat_badan = models.PositiveIntegerField()
    golongan_darah = models.CharField(max_length=2)
    catatan_kejahatan = models.CharField(max_length=255)
    nama_user = models.CharField(max_length=60)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    kewarganegaraan = models.CharField(max_length=50)
    agama = models.CharField(max_length=32)
    is_kawin = models.BooleanField(default=False)

    def unique_filename(self, filename):
        # Split the original filename and its extension
        base, extension = os.path.splitext(filename)
        # Generate a unique name using a timestamp and original extension
        unique_name = f'id_cards/{base}_{timezone.now().strftime("%Y%m%d%H%M%S")}{extension}'
        return unique_name
    
    gambar = models.ImageField(upload_to=unique_filename, null=True, blank=True)
    
    # Create a one-to-one relationship with the User model
    user_email_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_user

    class Meta:
        permissions = [
            ("view_profil_images", "Can view Profil images"),
        ]