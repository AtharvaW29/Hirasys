from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    # JSON field for socials
    # Image field for logo
    def __str__(self):
        return self.name