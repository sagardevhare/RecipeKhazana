from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(upload_to='recipe/')
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title
