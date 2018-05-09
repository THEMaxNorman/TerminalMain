from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Posting(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    header = models.CharField(max_length=25, blank = True)
    body = models.TextField(blank = True)
    time = models.DateTimeField(auto_now_add=True, null = True)
    active = models.BooleanField(default = True)
    catergory = models.CharField(blank = True, max_length = 40)
    airport = models.CharField(blank = True, max_length = 3)

class Massage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name = '+')
    text = models.TextField(blank = True)
    subject = models.ForeignKey(Posting, on_delete=models.CASCADE, null = True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    read = models.BooleanField(default = False)

class forum_topic(models.Model):
    airport = models.CharField(blank=True, max_length=3)
    title = models.CharField(max_length=45, blank = True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    catergories = (
        ("Delay Info", "Delay Info"),
        ("Things to do in the Area", "Things to do in the Area"),
        ("Airport Tips/Hacks", "Airport Tips/Hacks"),
        ("NTR", "NTR")
    )
    catregory = models.CharField(max_length = 50, choices = catergories)
class forum_post(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    text = models.TextField(blank=True)
    subject = models.ForeignKey(forum_topic, on_delete=models.CASCADE, null=True,)
    time = models.DateTimeField(auto_now_add=True, null=True)
    sticky = models.BooleanField(default = False)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rep = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


