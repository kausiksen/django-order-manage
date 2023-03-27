from django.db import models

# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    prodCode = models.CharField(max_length=20)
    custCode = models.CharField(max_length=20)
    isFav = models.BooleanField()
    image = models.CharField(max_length=20)

