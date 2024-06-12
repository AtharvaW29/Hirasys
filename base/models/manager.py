from django.contrib.auth.models import AbstractUser
from django.db import models

class HRManager(AbstractUser):
    role = models.CharField(max_length=255, default='HR Manager')  # Set default role
    created_jobs = models.ManyToManyField('Job', related_name='created_by')

    def __str__(self):
        return self.username
