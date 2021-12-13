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
    
    
class Profile(models.Model):
    profile_photo = CloudinaryField('profpics')
    bio = models.TextField(blank = True)
    user_id = models.OneToOneField(User, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_user(self):
        self.save()

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save,sender=User)
    def save_profile(sender,instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.url