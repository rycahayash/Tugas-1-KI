# Generated by Django 4.2.6 on 2023-10-16 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profil", "0003_remove_profil_user_id_user_alter_profil_is_kawin_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profil",
            name="gambar",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/id_cards"
            ),
        ),
    ]
