from django.db import models
from django.contrib.auth.models import User  # Import User model (modify if using a custom User model)
from . import Candidate, Job

class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('In Progress', 'In Progress'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Offered', 'Offered'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    scores = models.JSONField(blank=True, default=dict)  # Stores assessment scores
    cover_letter = models.TextField()
    interview_feedback = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Data isolation for HR managers

    def __str__(self):
        return f"{self.candidate.name} - {self.job.title}"
