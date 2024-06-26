# Create your models here.
from django.contrib.auth.models import User, Group
from django.db import models
   
class HRManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=[
        ('HRAdmin', 'HR Admin'),
        ('HR', 'HR'),
        ('HREmp', 'HR Employee')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to='manager/profile_pic', null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    class Meta:
        ordering = ('-created_at', )