from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    department = models.CharField(max_length=255)
    skills_required = models.TextField()  # Comma-separated skills list 
    applications = models.ManyToManyField('Application', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
