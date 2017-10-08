from django.db import models
import json

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class User(models.Model):
    name = models.CharField(max_length=27)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    expertise = models.ForeignKey('UserExpertise')
    description = models.TextField()
    email = models.EmailField(unique=True, db_index=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey('User')
    photo = models.ImageField('profile picture', upload_to='static/media/images/avatars/',
                                       null=True, blank=True)

    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar = "static/img/noprofile.svg"

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

    def setExpertise(self, expertise):
        self.expertise = json.dumps(expertise)

    def getExpertise(self):
        return json.loads(self.expertise)

    def __str__(self):
        return str(self.expertise)