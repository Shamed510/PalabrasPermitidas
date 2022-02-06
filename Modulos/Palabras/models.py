from django.db import models
import datetime
# Create your models here.

class Palabras(models.Model):
    stat = [
        ('Active', 'Active'),
        ('Deleted', 'Deleted')
    ]

    id = models.AutoField(primary_key = True)
    word = models.CharField(max_length = 50)
    allowed = models.BooleanField(default = True)
    status = models.CharField(max_length = 7, choices = stat, default = 'Active')
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    dateDeleted = models.DateTimeField(null=True, blank=True)