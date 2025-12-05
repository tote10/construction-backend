from rest_framework import serializers
from .models import Project, ProjectUpdate

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUpdate
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    updates = ProjectUpdateSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
