from django.contrib import admin

# Register your models here.
from apitest.models import ApiTestCase, Api, ApiStep


class ApiStepAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_param', 'api_method',
                    'api_result', 'api_status', 'create_time', 'id', 'api_case']
    model = ApiStep
    extra = 1


class ApiTestCaseAdmin(admin.ModelAdmin):
    list_display = ['api_case_name', 'api_case_desc', 'api_case_tester', 'api_case_result', 'create_time', 'id']
    inlines = [ApiStepAdmin]


class ApiAdmin(admin.ModelAdmin):
    list_display = ['api_name', 'api_url', 'api_param', 'api_method',
                    'api_result', 'api_status', 'create_time', 'id', 'product']


admin.site.register(ApiTestCase, ApiTestCaseAdmin)
admin.site.register(Api, ApiAdmin)

admin.site.site_title = '自动化测试平台'
admin.site.site_header = '自动化测试平台'
