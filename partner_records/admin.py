# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MedicalImage, EnvironmentFactor, Patient, DoctorNotes, PartnerRecord, PartnerConfig


@admin.register(MedicalImage)
class MedicalImageAdmin(admin.ModelAdmin):
    list_display = ('oplusid', 'image', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(EnvironmentFactor)
class EnvironmentFactorAdmin(admin.ModelAdmin):
    list_display = (
        'oplusid',
        'name',
        'description',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'oplusid',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(DoctorNotes)
class DoctorNotesAdmin(admin.ModelAdmin):
    list_display = (
        'oplusid',
        'title',
        'summary',
        'body',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(PartnerRecord)
class PartnerRecordAdmin(admin.ModelAdmin):
    list_display = (
        'oplusid',
        'partner_name',
        'mrn',
        'patient',
        'medical_images',
        'environment_factors',
        'doctor_notes',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'patient',
        'medical_images',
        'environment_factors',
        'doctor_notes',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'


@admin.register(PartnerConfig)
class PartnerConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner_name', 'connect_string')

from django import forms
class DoctorNotesForm( forms.ModelForm ):
    note = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = PartnerRecord
        fields = ('note',)
        widgets = {
            'note': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
