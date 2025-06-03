from rest_framework import serializers
from hobby.models import Hobby

class BasicHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'title']

class DetailedHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'title', 'banner', 'description', 'images']