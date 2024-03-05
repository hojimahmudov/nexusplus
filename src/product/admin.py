from django.contrib import admin
from .models import City, Category, Product, ProductImage

admin.site.register(City)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
