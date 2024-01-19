from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.URLField(
        default="https://lh3.googleusercontent.com/proxy/dDdc84j6O0gxfwK95HFTxmPjdMYO1rO9fPnGEDAIH-5eeKFc2u3W__V8of7b79aCc8TaWrv2vBf4r6o9Zg2R7BosdIOOtrXC0u7V74y8gg"
    )
    category = models.CharField(max_length=100, default="uncategorized")

    def __str__(self):
        return self.name
