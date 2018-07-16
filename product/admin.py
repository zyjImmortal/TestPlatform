from django.contrib import admin

# Register your models here.
from apitest.models import Api
from product.models import Product

class ApiAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_param', 'api_method',
                    'api_result', 'api_status', 'create_time', 'id', 'product']
    model = Api
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_desc', 'producter', 'create_time', 'id']
    inlines = [ApiAdmin]

admin.site.register(Product, ProductAdmin)