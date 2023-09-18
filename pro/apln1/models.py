from django.db import models

# Create your models here.
class book(models.Model):
    user = models.CharField(max_length=20)
    rollno = models.IntegerField()