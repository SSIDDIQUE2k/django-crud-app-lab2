from django.db import models
from django.urls import reverse

class Animal(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this animal's details
        return reverse('animal-detail', kwargs={'pk': self.id})