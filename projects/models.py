from django.db import models

class Project(models.Model):
    STATUS_CHOICES = (
        ('PL', 'Planned'),
        ('IP', 'In Progress'),
        ('CO', 'Completed'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    cover_image = models.ImageField(upload_to='project_cover/')
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='IP')

    def __str__(self):
        return self.name
class ProjectsUpdate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_image = models.ImageField(upload_to='project_updates/', null=True, blank=True)
    def __str__(self):
        return f"{self.title} - {self.project.name}"