
from djongo import models
from datetime import datetime

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.name
