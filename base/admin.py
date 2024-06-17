from django.contrib import admin
from .candidate import Candidate

# Register your models here.
class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ('candidate_id', 'name', 'email', 'phone', 'education', 'experiences', 'skills', 'application')

    def display_applications(self, obj):
        return ", ".join([f'{app.job_title} at {app.company_name} on {app.date_applied}' for app in obj.applications.all()])

    display_applications.short_description = 'Applications'

admin.site.register(Candidate, CandidateModelAdmin)
