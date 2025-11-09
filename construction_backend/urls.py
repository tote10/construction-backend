from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectViewSet
from services.views import ServiceViewSet
from vacancies.views import JobViewSet, ApplicationViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)
urlpattern = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
