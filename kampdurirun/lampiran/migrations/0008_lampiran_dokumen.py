# Generated by Django 4.2.6 on 2023-10-17 15:59

from django.db import migrations, models
import lampiran.models


class Migration(migrations.Migration):

    dependencies = [
        ("lampiran", "0007_alter_lampiran_dokumen_laporan"),
    ]

    operations = [
        migrations.AddField(
            model_name="lampiran",
            name="dokumen",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=lampiran.models.Lampiran.unique_filename,
            ),
        ),
    ]