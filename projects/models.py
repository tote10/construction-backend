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
    cover_image = models.ImageField(upload_to="projects/covers/", blank=True, null=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='IP')

    def __str__(self):
        return self.name
class ProjectUpdate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Project.STATUS_CHOICES, default='IP')
    update_image = models.ImageField(upload_to='project_updates/', null=True, blank=True)
    def __str__(self):
        return f"{self.title} - {self.project.name}"
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/images/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.project} - {self.caption or self.image.name}"