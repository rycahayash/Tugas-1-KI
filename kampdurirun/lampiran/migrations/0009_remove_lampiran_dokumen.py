# Generated by Django 4.2.6 on 2023-10-17 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lampiran", "0008_lampiran_dokumen"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lampiran",
            name="dokumen",
        ),
    ]
