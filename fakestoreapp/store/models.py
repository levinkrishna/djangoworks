from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)

class Products(models.model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    image=models.ImageField(upload_to="images")
    price=models.PositiveIntegerField()
    Category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)

class Carts(models.Model):
    Products=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Products=models.ForeignKey(Products,on_delete=models.CASCADE)
    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)

from django.core.validators import MinValueValidator,MaxValueValidator
class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Products=models.ForeignKey(Products,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)


