from django.db import models
from django.contrib.auth.models import User
# from portfolio.models import Writer

class Blog(models.Model):
    TAG = (
        ('Burnout', 'Burnout'),
        ('Beginners', 'Beginners'),
        ('Frameworks', 'Frameworks'),
        ('Interviews', 'Interviews'),
        ('JavaScript', 'JavaScript'),
        ('Programming', 'Programming'),
        ('Python', 'Python'),
        ('Soft Skills', 'Soft Skills'),
        ('Tutorial Hell', 'Tutorial Hell'),
    )
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, choices=TAG)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    body = models.TextField(max_length=3000)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
