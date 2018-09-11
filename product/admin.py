from django.contrib import admin

# Register your models here.
from api.models import Api
from product.models import Product, Env, Version


class ApiAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_param', 'api_method',
                    'api_result', 'api_status', 'create_time', 'id', 'product']
    model = Api
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_desc', 'producter', 'create_time', 'id']
    inlines = [ApiAdmin]


class EnvAdmin(admin.ModelAdmin):
    list_display = ['name', 'env_url']


class VersionAdmin(admin.ModelAdmin):
    list_display = ['version']


admin.site.register(Product, ProductAdmin)
admin.site.register(Env, EnvAdmin)
admin.site.register(Version, VersionAdmin)
