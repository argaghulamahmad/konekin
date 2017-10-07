# from django.db import models
# from django.forms import ImageField
# import os
# import json
#
# GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#
# def get_image_path(instance, filename):
#     return os.path.join('photos', str(instance.id), filename)
#
# class User(models.Model):
#     name = models.CharField(max_length=27)
#     birthday = models.DateField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     expertise = models.ForeignKey(UserExpertise)
#     description = models.TextField()
#     email = models.EmailField()
#
# class UserProfile(models.Model):
#     user = models.ForeignKey(User, unique=True)
#     photo = models.ForeignKey(Photo)
#
# class Photo(models.Model):
#     profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
#
# class UserPost(models.Model):
#     user = models.ForeignKey(User, unique=True)
#     activity = models.TextField(max_length=60)
#     date = models.DateTimeField()
#
# class UserExpertise(models.Model):
#     expertise = models.CharField(max_length=200)
#
#     def setExpertise(self, expertise):
#         self.expertise = json.dumps(expertise)
#
#     def getExpertise(self):
#         return json.loads(self.expertise)