from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import *
import pytz
from datetime import datetime
datetime.utcnow().replace(tzinfo=pytz.utc)

class MainUnitTest(TestCase):
    def test_model_can_create_new_user(self):
        # Creating a new user
        new_user = User.objects.create(name="Arga Ghulam Ahmad", birthday="1998-12-9", gender="M",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new user expertise
        new_user_expertise1 = UserExpertise(expertise="web development")
        new_user_expertise2 = UserExpertise(expertise="mobile apps development")
        new_user_expertise1.save()
        new_user_expertise2.save()
        new_user.expertise.add(new_user_expertise1, new_user_expertise2)

        # Retrieving all user
        counting_all_user = User.objects.all().count()
        self.assertEqual(counting_all_user, 1)

    def test_model_can_create_new_user_post(self):
        # Creating a new user
        new_user = User.objects.create(name="Arga Ghulam Ahmad", birthday="1998-12-9", gender="M",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new user expertise
        new_user_expertise1 = UserExpertise(expertise="web development")
        new_user_expertise2 = UserExpertise(expertise="mobile apps development")
        new_user_expertise1.save()
        new_user_expertise2.save()
        new_user.expertise.add(new_user_expertise1, new_user_expertise2)

        post_text = "Hai Semua! Belajar PPW Yuk :)"

        # Creating a new post
        new_post = UserPost.objects.create(user=new_user, post=post_text, date="2017-10-6 06:00:00+0800")


        # Retrieving all userpost
        counting_all_user_post = UserPost.objects.all().count()
        self.assertEqual(counting_all_user_post, 1)

    def test_model_can_create_new_user_expertise(self):
        # Creating a new user expertise
        new_user_expertise1 = UserExpertise(expertise="web development")
        new_user_expertise2 = UserExpertise(expertise="mobile apps development")
        new_user_expertise1.save()
        new_user_expertise2.save()

        # Retrieving all user expertise
        counting_all_user_expertise = UserExpertise.objects.all().count()
        self.assertEqual(counting_all_user_expertise, 2)

    def test_model_can_create_new_user_profile(self):
        # Creating a new user
        new_user = User.objects.create(name="Arga Ghulam Ahmad", birthday="1998-12-9", gender="M",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new user expertise
        new_user_expertise1 = UserExpertise(expertise="web development")
        new_user_expertise2 = UserExpertise(expertise="mobile apps development")
        new_user_expertise1.save()
        new_user_expertise2.save()
        new_user.expertise.add(new_user_expertise1, new_user_expertise2)

        # Creating a new user profile
        new_user_profile = UserProfile.objects.create(user=new_user)

        # Creating new profile photo
        new_user_profile.photo = SimpleUploadedFile(name='test_image.jpg', content=open('static/img/noprofile.svg', 'rb').read(),
                           content_type='image/jpeg')

        # Retrieving all user profile
        counting_all_user_profile = UserProfile.objects.all().count()
        self.assertEqual(counting_all_user_profile, 1)