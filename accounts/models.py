from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Post(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    discribe = models.TextField()
    prise = models.CharField(max_length=20)
    date_create = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete =models.CASCADE)
    discribe = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=30 ,default='')
    phone_number = models.IntegerField( default=0)
    image = models.ImageField(upload_to='profile_picture',blank=True)
    def __str__(self):
        return self.user.username

def create_profile(sender ,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile ,sender=User)