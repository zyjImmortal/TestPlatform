from django.contrib import admin

# Register your models here.
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_desc', 'producter', 'create_time', 'id']


admin.site.register(Product, ProductAdmin)