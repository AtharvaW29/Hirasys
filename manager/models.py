# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job

class HRManager(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user can belong to multiple groups.',
        related_name='hr_managers',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='hr_managers',
        verbose_name='user permissions'
    )
    role = models.CharField(max_length=255, default='HR Manager')  # Set default role
    created_jobs = models.ForeignKey(Job, related_name='created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role

    class Meta:
        ordering = ('-created_at', )