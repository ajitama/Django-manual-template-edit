from django.contrib import admin
from formman.models import TestMaster

# Register your models here.

class FormmanTestMasterAdmin(admin.ModelAdmin):
    list_display = (
            'test_pk',
            'id',
            'name',
            'number',
            )

admin.site.register(TestMaster, FormmanTestMasterAdmin)
