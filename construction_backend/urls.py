from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectUpdateViewSet, ProjectViewSet
from services.views import ServiceViewSet
from vacancies.views import JobViewSet, ApplicationViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'project-updates', ProjectUpdateViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
