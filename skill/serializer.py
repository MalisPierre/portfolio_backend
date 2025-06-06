from rest_framework import serializers
from skill.models import Skill

class VeryBasicMSkillSerializer(serializers.Serializer):
    title = serializers.CharField()
    release_date = serializers.DateField()


class BasicSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill__id', 'title', 'level', 'skill__icon']

class DetailedSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title', 'level', 'icon', 'banner', 'description', 
            'example', 'tips', 'experiences', 'display_title', 'color']