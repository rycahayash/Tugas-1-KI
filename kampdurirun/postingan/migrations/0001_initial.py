# Generated by Django 4.2.6 on 2023-10-15 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("lampiran", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Postingan",
            fields=[
                (
                    "id_postingan",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("judul", models.CharField(max_length=100)),
                ("waktu_upload", models.DateTimeField()),
                ("deskripsi", models.CharField(max_length=255)),
                ("is_public", models.BooleanField()),
                ("key", models.CharField(max_length=16)),
                (
                    "lampiran_id_lampiran",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lampiran.lampiran",
                    ),
                ),
                (
                    "user_email_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
