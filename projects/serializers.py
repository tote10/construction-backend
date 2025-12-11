from rest_framework import serializers
from .models import Project, ProjectUpdate, ProjectImage

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUpdate
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "caption"]

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False,
        allow_empty=True,
    )

    class Meta:
        model = Project
        fields = [
            "id", "name", "description", "cover_image",
            "start_date", "end_date", "images", "image_files",
        ]

    def create(self, validated_data):
        image_files = validated_data.pop("image_files", [])
        project = super().create(validated_data)
        for image_file in image_files:
            ProjectImage.objects.create(project=project, image=image_file)
        return project

    def update(self, instance, validated_data):
        image_files = validated_data.pop("image_files", [])
        project = super().update(instance, validated_data)
        for image_file in image_files:
            ProjectImage.objects.create(project=project, image=image_file)
        return project
