from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    project_photo = CloudinaryField('projectpics/')
    description = models.TextField(max_length=400,blank=True)
    github_repo = models.CharField(max_length=150, blank=True)
    url = models.CharField(max_length=60,blank=True)
    uploader = models.ForeignKey(User, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.url