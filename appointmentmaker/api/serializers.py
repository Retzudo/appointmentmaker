from rest_framework import serializers

from core import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'
        read_only_fields = ('owner',)


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        exclude = ('internal_notes',)
        read_only_fields = ('creator',)
