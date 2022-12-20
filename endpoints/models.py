from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class postDetails(models.Model):
    profileName = models.CharField(max_length = 50)
    profileImage = models.URLField()
    profileDescription = models.TextField()
    tags = ArrayField(models.CharField(max_length = 50),default=list)
    imageUrl = models.TextField()
    projectName = models.CharField(max_length = 50)
    projectGist = models.TextField()
    projectDescription = models.TextField()