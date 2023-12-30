# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    Product_img = models.URLField()

    def __str__(self):
        return self.name
