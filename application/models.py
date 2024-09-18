from django.db import models
from django.contrib.auth.models import User
from base.models import Candidate
from jobs.models import Job

class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('In Progress', 'In Progress'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Offered', 'Offered'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    scores = models.JSONField(blank=True, default=dict)
    cover_letter = models.CharField(max_length=500)
    interview_feedback = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)  # Data isolation for HR managers
    application_date = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications", null=True, blank=True)

    def __str__(self):
        return f"{self.application_id} - {self.applied_to_job}"
    
    class Meta:
        ordering = ('-application_date', )
