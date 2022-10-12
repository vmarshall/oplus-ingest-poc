from django.contrib.auth.models import User, Group
from rest_framework import serializers
from hospital.models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'