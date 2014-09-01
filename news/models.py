#coding=utf8
from django.db import models
# Create your models here.
# 发出的实时消息
class Tweets(models.Model):
        usename = models.CharField(max_length=30)
        content= models.CharField(max_length=140)
class Followed(models.Model):
        usename = models.CharField(max_length=30)
        followedname = models.CharField(max_length=30)

class Following(models.Model):
        usename = models.CharField(max_length=30)
        followingname = models.CharField(max_length=30)
