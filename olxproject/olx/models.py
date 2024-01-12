from django.db import models

# Create your models here.


class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    number=models.CharField(max_length=30)
    owner=models.CharField(max_length=20)
    km=models.CharField(max_length=20)
    vehiclemodel=models.CharField(max_length=4)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name