from django.contrib.auth.models import User
from django.db import models
from company.models import Company

class HRManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, default='')
    role = models.CharField(max_length=50, choices=[
        ('HRAdmin', 'HR Admin'),
        ('HR', 'HR'),
        ('Employee', 'Employee')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    class Meta:
        ordering = ('-created_at', )
