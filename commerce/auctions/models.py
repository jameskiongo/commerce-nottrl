from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.URLField(
        max_length=255,
        default="https://curie.pnnl.gov/sites/default/files/default_images/default-image_0.jpeg",
    )
    category = models.CharField(max_length=100, default="uncategorized")

    def __str__(self):
        return self.name
