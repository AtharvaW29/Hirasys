from django.contrib import admin
from .models.candidate import Candidate

# Register your models here.
class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'get_skills', 'get_experiences', 'get_applications']

    def get_skills(self, obj):
        return ", ".join([skill.skill for skill in obj.skills.all()])

    def get_experiences(self, obj):
        return ", ".join([f"{exp.title} at {exp.company}" for exp in obj.experiences.all()])

    def get_applications(self, obj):
        return ", ".join([f"{app.job_title} at {app.company_name}" for app in obj.applications.all()])

    get_skills.short_description = 'Skills'
    get_experiences.short_description = 'Experiences'
    get_applications.short_description = 'Applications'

admin.site.register(Candidate, CandidateModelAdmin)