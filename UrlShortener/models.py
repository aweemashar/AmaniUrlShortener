from django.db import models
from django.utils import timezone


# Create your models here.
class URLS(models.Model):
    original_url = models.CharField(max_length=256)
    shorten_url = models.CharField(max_length=15, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "URLS"
