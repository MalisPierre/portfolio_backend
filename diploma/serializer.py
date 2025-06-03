from rest_framework import serializers
from diploma.models import Diploma

class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = ['id', 'title', 'description', 'date']