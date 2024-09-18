from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from manager.models import HRManager

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    employement_type = models.CharField(max_length=20)
    department = models.CharField(max_length=255)
    skills_required = models.JSONField()
    application_start_date = models.DateTimeField(default=datetime.now)
    application_end_date = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(HRManager, on_delete=models.CASCADE, related_name='created_jobs')

    def clean(self):
        # Validation for start and end dates
        if self.application_start_date and self.application_end_date:
            if self.application_end_date <= self.application_start_date:
                raise ValidationError({'application_end_date': 'End date must be after start date.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Calls the clean method to validate data
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
