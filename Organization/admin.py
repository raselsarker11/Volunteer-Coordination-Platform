from django.contrib import admin
from . models import Opportunity, Organization, Volunteer

# Register your models here.

admin.site.register(Opportunity)
admin.site.register(Organization)
admin.site.register(Volunteer)