from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings 


class Problem_kd(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User',db_index=True)
    title = models.CharField(max_length=200,blank=False,null=False)
    text = models.TextField(blank=False)
    created_date = models.DateTimeField(
            default=timezone.now,db_index=True)
    date_chng = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
    kd = models.CharField(max_length=50,blank=False,null=False,db_index=True)
    
    state_choices = (('solved','solved'),('not_solved','not_solved'),('questions','questions'))
    state_kd = models.CharField(max_length=50,choices=state_choices,default='not_solved')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class UserProfile(models.Model):
   
    user = models.OneToOneField(User,null=True, blank=True)
    
    
    skill = models.CharField(blank=False, null=False, max_length=200)
    
    
    def __unicode__(self):
        return self.user.username
