from django.contrib import admin

from app.models import AppCase, AppCaseStep


# Register your models here.

class AppCaseStepAdmin(admin.TabularInline):
    list_display = ['app_test_step', 'app_test_obj_name', 'app_element', 'app_find_method',
                    'app_test_data', 'app_assert_data', 'app_test_result', 'id', 'app_case']
    model = AppCaseStep
    extra = 1


class AppCaseAdmin(admin.ModelAdmin):
    list_display = ['app_case_name', 'app_test_result', 'app_tester', 'create_time', 'id']
    inlines = [AppCaseStepAdmin]


admin.site.register(AppCase, AppCaseAdmin)
