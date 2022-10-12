import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class MedicalImage(models.Model):
    oplusid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






class EnvironmentFactor(models.Model):
    oplusid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, default=None, max_length=500, help_text="Doctor's notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s %s" % (self.name, self.description)


class Patient(models.Model):
    oplusid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.email, self.phone_number)


class DoctorNotes(models.Model):
    oplusid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True, default=None, max_length=500, help_text="Doctor's notes")
    body = models.TextField(blank=True, null=True, default=None, max_length=500, help_text="Doctor's notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.title, self.summary, self.body)



class PartnerRecord(models.Model):
    oplusid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partner_name = models.CharField(max_length=200, blank=False)
    mrn = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True, default=None)
    medical_images = models.ForeignKey(MedicalImage, on_delete=models.CASCADE, related_name='medical_images', blank=True, null=True)
    environment_factors = models.ForeignKey(EnvironmentFactor, max_length=200, on_delete=models.CASCADE, related_name='environment_factors', blank=True, null=True)
    doctor_notes = models.ForeignKey(DoctorNotes, on_delete=models.CASCADE, related_name='doctor_notes', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.partner_name


class PartnerConfig(models.Model):
    partner_name = models.CharField(max_length=200, blank=False)
    connect_string = models.CharField(max_length=200, blank=False)