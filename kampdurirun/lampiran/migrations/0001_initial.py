# Generated by Django 4.2.6 on 2023-10-15 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lampiran",
            fields=[
                (
                    "id_lampiran",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "jenis_lampiran",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("video", "Video"),
                            ("document", "Document"),
                        ],
                        default="image",
                        max_length=8,
                    ),
                ),
                ("dokumen_laporan", models.FileField(upload_to="lampiran/")),
                (
                    "metode_crypto",
                    models.CharField(
                        choices=[
                            ("aes-csb", "AES-CBC"),
                            ("aes-cfb", "AES-CFB"),
                            ("aes-ofb", "AES-OFB"),
                            ("aes-ctr", "AES-CTR"),
                            ("rc4", "RC4"),
                            ("des-csb", "DES-CBC"),
                            ("des-cfb", "DES-CFB"),
                            ("des-ofb", "DES-OFB"),
                            ("des-ctr", "DES-CTR"),
                        ],
                        default="aes-csb",
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
