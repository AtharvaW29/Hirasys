from django.contrib import admin
from .models import TestModel
# Register your models here.

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')