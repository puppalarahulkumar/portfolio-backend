from rest_framework import serializers
from .models import ProjectModel,HeroModel,AboutSectionModel,CommunityModel,ContactUsModel


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectModel
        fields="__all__"

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        fields = '__all__'


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSectionModel
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityModel
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = '__all__'
