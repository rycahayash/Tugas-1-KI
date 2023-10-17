from django.db import models
import os
from django.utils import timezone
import uuid

class Lampiran(models.Model):
    JENIS_LAMPIRAN_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    )
    METODE_CRYPTO_CHOICES = (
        ('aes-cbc', 'AES-CBC'),
        ('aes-cfb', 'AES-CFB'),
        ('aes-ofb', 'AES-OFB'),
        ('aes-ctr', 'AES-CTR'),
        ('rc4-txt', 'RC4 TEXT'),
        ('rc4-img', 'RC4 FILE'),
        ('des-csb', 'DES-CBC'),
        ('des-cfb', 'DES-CFB'),
        ('des-ofb', 'DES-OFB'),
    )

    id_lampiran = models.AutoField(primary_key=True)
    jenis_lampiran = models.CharField(
        max_length=8,
        choices=JENIS_LAMPIRAN_CHOICES,
        default='image'
    )

    def unique_filename(self, filename):
        base, extension = os.path.splitext(filename)
        unique_name = f'lampiran/{base}_{timezone.now().strftime("%Y%m%d%H%M%S")}{extension}'
        return unique_name
    
    def generate_custom_uuid():
        custom_uuid = uuid.uuid4()
        custom_uuid_str = str(custom_uuid).replace("-", "")
        return custom_uuid_str[:32]
    
    key = models.CharField(max_length=32, default=generate_custom_uuid, editable=False)
    dokumen_laporan = models.BinaryField(null=True, blank=True, editable=True)
    metode_crypto = models.CharField(
        max_length=10,
        choices=METODE_CRYPTO_CHOICES,
        default='aes-csb'
    )
    
    key_crypto = models.CharField(max_length=32, default=generate_custom_uuid, editable=False)
    pro_crypto = models.CharField(max_length=32, default=generate_custom_uuid, editable=False)

    def __str__(self):
        return str(self.id_lampiran)

    class Meta:
        unique_together = ('key', 'id_lampiran')
