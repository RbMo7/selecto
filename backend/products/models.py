# models.py
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_img = models.URLField()

    def __str__(self):
        return self.name
