from django.contrib import admin

# Register your models here.
from .models import Facility


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'facility_name',
        'bin',
        'latitude',
        'longitude',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'