from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)
    Bio = models.TextField(max_length=150, null=True)
    Location = models.CharField(max_length=150)
    Work = models.TextField(max_length=150)

    def __str__(self):
        return self.Name