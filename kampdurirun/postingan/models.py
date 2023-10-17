from django.db import models
from user.models import User

class Postingan(models.Model):
    id_postingan = models.AutoField(primary_key=True)  # Change to AutoField
    judul = models.CharField(max_length=100)
    waktu_upload = models.DateTimeField(auto_now_add=True)
    deskripsi = models.CharField(max_length=255)
    key = models.CharField(max_length=16)
    
    # Define a foreign key to the User model
    user_email_user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Define a foreign key to the Lampiran model
    lampiran_id_lampiran = models.OneToOneField('lampiran.Lampiran', on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
