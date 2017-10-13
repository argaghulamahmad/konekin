# Create your models here.
from django.db import models

class UpStatus(models.Model):
        description = models.TextField()
        created_date = models.DateTimeField(auto_now_add=True)