import datetime

from django.db import models
from time import gmtime, strftime
# Create your models here.


class Articles(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    Title = models.CharField(max_length=1000, null=False)
    Image = models.ImageField(max_length=1000)
    HeaderImage = models.CharField(max_length=255, null=False)
    Introduction = models.CharField(max_length=255, null=False)
    Description = models.CharField(max_length=255, null=False)
    LastMod = models.DateField(default=strftime("%d %B %Y"))
    Language = models.CharField(max_length=255, null=False)
    KeyWords = models.CharField(max_length=255, null=False)
    State = models.IntegerField(null=False)
    NumVisit = models.IntegerField(null=False)
    IdTheme = models.IntegerField(null=False)
    IdUser = models.IntegerField(null=False)
    IdHost = models.IntegerField(null=False)


