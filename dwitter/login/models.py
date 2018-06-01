from django.db import models
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    User_Name = models.CharField(unique = True , max_length = 200 )
    email = models.CharField(unique = True , max_length = 200)
    password = models.CharField(max_length = 8)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    birth_date = models.DateField()

class Dweet(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE )
    Content = models.TextField()
    time = models.DateTimeField()
#class Follower():
 #   user_id = models.ForeignKey(Profile, on_delete=models.CASCADE )
  #  Follower_Id = models.ForeignKey(Profile, on_delete = models.CASCADE)
   # No_of_followers = models.IntegerField()


