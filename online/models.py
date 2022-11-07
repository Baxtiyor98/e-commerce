from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Products/%d/%m/%Y")
    price = models.FloatField()

    def __str__(self):
        return self.name

