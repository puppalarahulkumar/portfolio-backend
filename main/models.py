from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models import JSONField
# Create your models here.
class ProjectModel(models.Model):
    title=models.CharField(max_length=255)
    image = CloudinaryField('image',blank=True, null=True)
    content=models.JSONField(default=list)
    tech=models.JSONField(default=list)
    giturl=models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.title

class HeroModel(models.Model):
    name=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    intro=models.CharField(max_length=255)
    content=models.JSONField(default=list,blank=True,null=True)

    def __str__(self):
        return self.name

class AboutSectionModel(models.Model):
    bio=models.CharField(max_length=255)
    current_focus=models.CharField(max_length=255)
    hobbies=models.CharField(max_length=255)
    content=models.JSONField(default=list,blank=True,null=True)
    def __str__(self):
        return self.bio

class CommunityModel(models.Model):
    discord_url=models.CharField(max_length=255,null=True,blank=True)
    linkedin_newletter=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    content=models.JSONField(default=list,blank=True,null=True)
    def __str__(self):
        return self.linkedin_newletter

class ContactUsModel(models.Model):
    email=models.EmailField()
    phone=models.CharField(max_length=15,null=True,blank=True)
    linkedin=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    def __str__(self):
        return self.email
