from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import *

class MainUnitTest(TestCase):
    def test_model_can_create_new_user(self):
        # Creating a new user
        new_user = User.objects.create(name="Arga Ghulam Ahmad", birthday="9-12-1998", gender="M",
                                       expertise="gaming programming",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Retrieving all user
        counting_all_user = User.objects.all().count()
        self.assertEqual(counting_all_user, 1)

    def test_model_can_create_new_user_post(self):
        # Creating a new user
        new_user = User.objects.create(name="Arga Ghulam Ahmad", birthday="9-12-1998", gender="M",
                                       expertise="gaming programming",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new post
        post_text = "Hai Semua! Belajar PPW Yuk :)"

        # Creating a new post
        new_post = UserPost.objects.create(new_user, post_text, "6-10-2017")

        # Retrieving all available activity
        counting_all_user_post = UserPost.objects.all().count()
        self.assertEqual(counting_all_user_post, 1)

    def test_add_photo(self):
        newPhoto = Photo()
        newPhoto.image = SimpleUploadedFile(name='test_image.jpg',
                                            content=open('static/img/noprofile.svg', 'rb').read(),
                                            content_type='image/jpeg')
        newPhoto.save()
        self.assertEqual(Photo.objects.count(), 1)

    def test_model_can_create_new_user_expertise(self):
        # Creating a new user expertise
        expertise = "programming gaming"
        new_user_expertise = UserExpertise.objects.create(expertise)

        # Retrieving all available activity
        counting_all_user_expertise = UserExpertise.objects.all().count()
        self.assertEqual(counting_all_user_expertise, 1)

    def test_model_can_create_new_user_profile(self):
        # Creating a new user
        new_user = User.objects.create(name="Arga Ghulam Ahmad", birthday="9-12-1998", gender="M",
                                       expertise="gaming programming",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new image
        image = SimpleUploadedFile(name='test_image.jpg', content=open('static/img/noprofile.svg', 'rb').read(),
                                   content_type='image/jpeg')

        # Creating a new user profile
        new_user_profile = UserProfile.objects.create(new_user, image)

        # Retrieving all user profile
        counting_all_user_profile = UserProfile.objects.all().count()
        self.assertEqual(counting_all_user_profile, 1)