from rest_framework import viewsets
from .models import job, Application
from .serializers import JobSerializer, ApplicationSerializer
class JobViewSet(viewsets.ModelViewSet):
    queryset = job.objects.all()
    serializer_class = JobSerializer   
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer    