from django.db import models
from django.conf import settings


class Plan(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_planed_to_start = models.DateTimeField()
    date_planed_to_finish = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
