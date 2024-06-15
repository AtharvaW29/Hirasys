from django.contrib import admin
from .models.candidate import Candidate, Education, Experience, Skill, Application

# Register your models here.
class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'display_education', 'display_experiences', 'display_skills', 'display_applications')

    def display_education(self, obj):
        return ", ".join([f'{edu.degree} in {edu.major} from {edu.university}' for edu in obj.education.all()])

    def display_experiences(self, obj):
        return ", ".join([f'{exp.title} at {exp.company} for {exp.duration}' for exp in obj.experiences.all()])

    def display_skills(self, obj):
        return ", ".join([skill.skill for skill in obj.skills.all()])

    def display_applications(self, obj):
        return ", ".join([f'{app.job_title} at {app.company_name} on {app.date_applied}' for app in obj.applications.all()])

    display_education.short_description = 'Education'
    display_experiences.short_description = 'Experiences'
    display_skills.short_description = 'Skills'
    display_applications.short_description = 'Applications'

admin.site.register(Candidate, CandidateModelAdmin)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Application)