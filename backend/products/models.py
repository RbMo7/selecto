from django.db import models

class AmazonReview(models.Model):
    product_name = models.CharField(max_length=255)
    review_text = models.TextField()