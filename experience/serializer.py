from rest_framework import serializers
from experience.models import Experience

class BasicExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'job_title', 'contract_type', 'company_name', 'start_date']

class DetailedExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'job_title', 'contract_type', 'company_name', 'start_date', 'end_date', 'localisation', 'banner', 'description', 'tasks', "skills"]