from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
'''class Profile(models.Model):
    User_Name = models.CharField(unique = True , max_length = 200 )
    email = models.CharField(unique = True , max_length = 200)
    password = models.CharField(max_length = 8)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    birth_date = models.DateField()'''

class Dweet(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE )
    dweet = models.TextField()
    time = models.DateTimeField()

class Likes(models.Model):
    Liker_id = models.ForeignKey(User,on_delete = models.CASCADE)
    time = models.DateTimeField()

class Follower(models.Model):
    Fol_Id = models.ForeignKey(User,on_delete = models.CASCADE)
    time = models.DateTimeField()
    n_follower = models.ManyToManyField('self', related_name='follows', symmetrical=False)

class Comment(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField()

'''class Chat(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    Msg_sender = models.TextField()
    Msg_receiver = models.TextField()
    time = models.DateTimeField()
    sent_time = models.DateTimeField(default = timezone.now)'''

