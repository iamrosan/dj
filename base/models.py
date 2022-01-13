from django.db import models
from django.conf import settings


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # participants
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta: #for arranging to get the new room created appeared at the top
        ordering = ['-updated','-created'] #'-updated' for descending and 'updated' for ascending 

class Message(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    room =models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    body =models.TextField()

    def __str__(self):
        return self.body[:50]
