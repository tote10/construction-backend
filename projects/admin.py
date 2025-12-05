from django.contrib import admin
from .models import Project, ProjectUpdate

class ProjectUpdateInline(admin.TabularInline):
    model = ProjectUpdate
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectUpdateInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUpdate)
