from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Categories(models.Model):
    cid = models.CharField(max_length = 10, primary_key = True)
    cname = models.CharField(max_length = 50)
    def __str__(self):
        return self.cid
        
class Book_List(models.Model):
    Bid = models.CharField(max_length = 10,primary_key = True)
    Bname = models.CharField(max_length = 100)
    cid = models.ForeignKey('Categories') 
    def __str__(self):
        return self.Bid
class Author(models.Model):
    Aid = models.CharField(max_length = 10, primary_key = True)
    Aname = models.CharField(max_length = 70)
    def __str__(self):
        return self.Aid
class Book_Author(models.Model):
    Bid = models.ForeignKey('Book_List')
    Aid = models.ForeignKey('Author')
    def __str__(self):
        return self.Bid
class Book_details(models.Model):
    Bid = models.ForeignKey('Book_List')   
    price = models.IntegerField(max_length = 100,default = 1)
    rate = models.IntegerField(max_length = 100,default = 1)
    def __str__(self):
        return self.rate

    





    #rating = models.IntegerField()
'''class Wishlist(models.Model):
    uid = models.CharField(max_length = 10)
    #Bid = models.ForeignKey('Book_List')

    #price = models.ForeignKey('Book_List')
    def __str__(self):
        return self.uid
class Delivery(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    phNo = models.CharField(max_length = 12)
    email = models.CharField(max_length = 20)
    def __str__(self):
        return self.name
# Create your models here.'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    fname = models.CharField(max_length = 100)
    mname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    lname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    is_self_ratting = models.BooleanField(default = False)
    is_registered = models.BooleanField(default = False)
    is_pwd_reset = models.BooleanField(default = False)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
@receiver(post_save, sender=User)
def sender_user_profile(sender, instance, **kwargs):
    instance.profile.save()
