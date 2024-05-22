from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, OpportunityViewSet, VolunteerViewSet

router = DefaultRouter()
router.register('organization', OrganizationViewSet)
router.register('opportunity', OpportunityViewSet)
router.register('Volunteer', VolunteerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
