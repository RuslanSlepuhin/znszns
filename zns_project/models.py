from django.db import models


# Create your models here.
class Contacts(models.Model):
    title = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=15, default='')
    description = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=50, default='')
    text_title = models.CharField(max_length=100, default='')
    text_text = models.TextField(blank=True, default='')
    time_create = models.DateTimeField(auto_now_add=True)
    Time_update = models.DateTimeField(auto_now=True)


