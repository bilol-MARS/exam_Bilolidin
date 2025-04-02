from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass 


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/products/')
    rating = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"



class Saqlovchi(models.Model):
    message = models.TextField()
    def __str__(self):
        return self.message






class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product.name

       
