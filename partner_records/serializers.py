from django.contrib.auth.models import User, Group
from rest_framework import serializers

from partner_records.models import PartnerRecord


class PartnerRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerRecord
        fields = '__all__'