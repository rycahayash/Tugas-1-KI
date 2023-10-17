from django.db import models
from user.models import User

class Id_Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gambar = models.ImageField(upload_to='id_cards')

    def __str__(self):
        return str(self.user)