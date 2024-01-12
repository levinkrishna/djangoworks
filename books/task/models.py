from django.db import models

# Create your models here.

class Books(models.Model):
    name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    price=models.IntegerField()
    category=models.CharField(max_length=200)


    def _str_(self):
        return self.name
