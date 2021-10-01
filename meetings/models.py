from django.db import models

# Create your models here.
class Meeting(models.Model):
    title = models.CharField('Meeting Title', max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField('Meeting Start time')
    end_time = models.DateTimeField('Meeting End time')