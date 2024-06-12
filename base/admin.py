from django.contrib import admin
from .models.candidate import Candidate

# Register your models here.
@admin.register(Candidate)
class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'education', 'experiences', 'skills', 'applications')
