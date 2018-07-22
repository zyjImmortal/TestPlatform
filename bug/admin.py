from django.contrib import admin

# Register your models here.
from bug.models import Bug


class BugAdmin(admin.ModelAdmin):
    list_display = ['bug_name', 'bug_detail', 'bug_status', 'bug_level','bug_creater',
                    'bug_assign', 'created_time', 'id']


admin.site.register(Bug, BugAdmin)