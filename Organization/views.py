from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organization, Opportunity, Volunteer
from .serializers import OrganizationSerializer, OpportunitySerializer, VolunteerSerializer

# Create your views here.

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = [IsAuthenticated]
    

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Volunteer.objects.all() # retrieve korbo sob gulo objects k
        username = self.request.query_params.get('username', None)  # retrieve korlam query params k
        if username is not None:
            queryset = queryset.filter(volunteer__username=username)  # fillter korlam queryset username thakay
        return queryset  # return korlam oi queryset ta
