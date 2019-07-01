from django.db import models
from django import forms

# Create your models here.
class Visitor(models.Model):
    title = models.CharField(max_length = 255)
    image = models.FileField(upload_to = 'images/')
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.description[:20]