from django.db import models

# Create your models here.
class Tickets(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    movie_id=models.CharField(max_length=255)
    desc=models.TextField()
    profile_image=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    objects=models.Manager()