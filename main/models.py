from datetime import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=10, null=True)
    subject = models.CharField(max_length=20)
    grade = models.TextField()
    term = models.TextField(null=True)
    created_at = models.DateTimeField(default= timezone.now())
    