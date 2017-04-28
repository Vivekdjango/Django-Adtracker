from __future__ import unicode_literals

from django.db import models

import os

def get_image_path(instance, filename):
	return os.path.join('/home/vivek/django/spark/dream/static/images', str(instance.id), filename)

class UserProfile(models.Model):
   # user = models.ForeignKey(User, unique=True)
    	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	def __str__(self):
		return "%s"%(self.profile_image)

class data(models.Model):
	cn = models.IntegerField()
	def __str__(self):
		return "%d"%(self.cn)
# Create your models here.
