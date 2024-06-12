
from djongo import models
from datetime import datetime
from django.core.validators import RegexValidator

#Test model
# class TestModel(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(default=datetime.now, editable=False)

#     def __str__(self):
#         return self.name

# Embedded model for Application
class Application(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    date_applied = models.DateField(default=datetime.now)

    class Meta:
        abstract = True

#Embedded model for skills
class Skills(models.Model):
    skill = models.CharField(max_length=100)

    class Meta:
        abstract = True

# Candidate model

class Candidate(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}',
        message="Invalid Phone Number"
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    education = models.JSONField(blank=True, default=dict)
    experiences = models.JSONField(blank=True, default=dict)
    skills = models.ArrayField(model_container=Skills)
    applications = models.ArrayField(model_container=Application)

    def __str__(self):
        return self.name