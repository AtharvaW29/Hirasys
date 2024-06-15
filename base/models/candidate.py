from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Application(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    date_applied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Skill(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill

class Education(models.Model):
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    university = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.university}"

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Candidate(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$',
        message="Invalid Phone Number"
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name="candidates")
    experiences = models.ManyToManyField(Experience)
    skills = models.ManyToManyField(Skill)
    applications = models.ManyToManyField(Application)

    def __str__(self):
        return self.name