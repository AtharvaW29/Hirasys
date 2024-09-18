from django.db import models
from django.core.validators import RegexValidator

class Candidate(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$',
        message="Invalid Phone Number"
    )
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    education = models.JSONField()
    experiences = models.JSONField(blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name
