from django.db import models
from accounts.models import User

# Create your models here.


class HR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bpm = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class AverageHR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hour = models.IntegerField()
    avg_bpm = models.IntegerField()
