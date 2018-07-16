from django.contrib import admin

# Register your models here.
from apitest.models import ApiTestCase, Api


class ApiAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_param', 'api_method',
                    'api_result', 'api_status', 'create_time', 'id', 'api_case']
    model = Api
    extra = 1

class ApiTestCaseAdmin(admin.ModelAdmin):
    list_display = ['api_case_name', 'api_case_desc', 'api_case_tester', 'api_case_result', 'create_time', 'id']
    inlines = [ApiAdmin]


admin.site.register(ApiTestCase, ApiTestCaseAdmin)
# admin.site.register(Api, ApiAdmin)
