from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('grade_8', 'Grade 8'),
        ('grade_7', 'Grade 7'),
        ('grade_6', 'Grade 6'),
        ('grade_5', 'Grade 5'),
        ('teacher', 'Teacher'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='parent')
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
    
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_link = models.URLField()
    grade_level = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    file_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class Tutor(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    availability = models.TextField()
    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()
    Official = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Vacancy(models.Model):
    position = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    logo = models.ImageField()
    form = models.CharField(max_length=100)
    description = models.TextField()
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
