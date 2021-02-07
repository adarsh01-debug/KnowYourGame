from django.db import models

# Create your models here.
class Requirements(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=50)
    CPU = models.TextField(max_length=100)
    RAM = models.CharField(max_length=50)
    GPU = models.TextField(max_length=100)
    HDD = models.TextField(max_length=100)
    OS = models.TextField(max_length=100)

    def __str__(self):
        return self.name
