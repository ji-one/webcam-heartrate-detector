from django.db import models
from accounts.models import User

# Create your models here.
class HR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bpm = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
