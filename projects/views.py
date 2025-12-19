from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Project, ProjectUpdate
from .serializers import ProjectSerializer, ProjectUpdateSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

@extend_schema(
    request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'description': {'type': 'string'},
                'start_date': {'type': 'string', 'format': 'date'},
                'end_date': {'type': 'string', 'format': 'date'},
                'status': {'type': 'string', 'enum': ['PL', 'IP', 'CO']},
                'cover_image': {'type': 'string', 'format': 'binary'},
                'image_files': {
                    'type': 'array',
                    'items': {'type': 'string', 'format': 'binary'}
                }
            },
            'required': ['name', 'description', 'start_date']
        }
    }
)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    filterset_fields = ['status']
    search_fields = ['name', 'description']

@extend_schema(
    request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'title': {'type': 'string'},
                'content': {'type': 'string'},
                'project': {'type': 'integer'},
                'status': {'type': 'string', 'enum': ['PL', 'IP', 'CO']},
                'update_image': {'type': 'string', 'format': 'binary'},
            },
            'required': ['title', 'content', 'project']
        }
    }
)
class ProjectUpdateViewSet(viewsets.ModelViewSet):
    queryset = ProjectUpdate.objects.all()
    serializer_class = ProjectUpdateSerializer
