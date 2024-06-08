from django.db import models

# Create your db models here.
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    education = models.JSONField(blank=True, default=dict)  # Stores education details as a dictionary

    experiences = models.JSONField(blank=True, default=dict)  # Stores experience details as a dictionary
    skills = models.CharField(max_length=255, blank=True)  # Comma-separated skills list 
    applications = models.ManyToManyField('Application', on_delete=models.CASCADE)

    def __str__(self):
        return self.name