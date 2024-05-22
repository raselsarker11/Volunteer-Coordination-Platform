
from rest_framework import serializers
from .models import  Organization, Opportunity, Volunteer



class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'mission', 'contact_info']


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'organization', 'title', 'description', 'date', 'location', 'required_skills']


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id', 'opportunity', 'volunteer', 'registration_date', 'status']
