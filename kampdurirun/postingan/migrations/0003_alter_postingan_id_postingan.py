# Generated by Django 4.2.6 on 2023-10-17 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postingan", "0002_alter_postingan_waktu_upload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postingan",
            name="id_postingan",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]