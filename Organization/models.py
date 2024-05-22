from django.db import models
from account.models import User
from .status import STATUS_CHOICES

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    required_skills = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Volunteer(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    volunteer_details = models.TextField(max_length= 255, null=True, blank=True)

    def __str__(self):
        return self.volunteer.email
