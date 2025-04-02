from django.contrib import admin
from .models import Product, User, WishList, Saqlovchi

# Register your models here.

admin.site.register(Product)
admin.site.register(User)
admin.site.register(WishList)
admin.site.register(Saqlovchi)