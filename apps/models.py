from django.db import models

# Create your models here.


# Create your models here.
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