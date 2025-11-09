from rest_framework import serializers
from .models import job, Application
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'  