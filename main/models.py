from django.db import models
import datetime
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class User(models.Model):
    name = models.CharField(max_length=27)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    expertise = models.ManyToManyField('UserExpertise')
    friend = models.ManyToManyField('UserFriend')
    description = models.TextField()
    email = models.EmailField(unique=True, db_index=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey('User')
    photo = models.ImageField('profile picture', upload_to='static/media/images/avatars/',
                                       null=True, blank=True, default="static/img/noprofile.svg")

    def __str__(self):
        return self.user.name

class UserPost(models.Model):
    user = models.ForeignKey('User')
    post = models.TextField(max_length=140)
    date = models.DateTimeField()

    def __str__(self):
        return self.user.name + " " + str(self.date)

class UserExpertise(models.Model):
    expertise = models.CharField(max_length=200)

    def __str__(self):
        return str(self.expertise)

class UserFriend(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    date= models.DateTimeField(auto_now_add = True)

    # def __str__(self):
    #     return str(self.name + " " + self.url + " Added since " + datetime.datetime.strptime(str(self.date), '%Y-%m-%d %H:%M:%S'))