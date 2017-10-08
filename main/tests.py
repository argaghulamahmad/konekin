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

        # Creating a new user friends
        new_user_friend1 = UserFriend(name="Arga Ghulam Ahmad", url="https://ppw-lab-arga.herokuapp.com/")
        new_user_friend2 = UserFriend(name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/")
        new_user_friend1.save()
        new_user_friend2.save()
        new_user.friend.add(new_user_friend1, new_user_friend2)

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

        # Creating a new user friends
        new_user_friend1 = UserFriend(name="Arga Ghulam Ahmad", url="https://ppw-lab-arga.herokuapp.com/")
        new_user_friend2 = UserFriend(name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/")
        new_user_friend1.save()
        new_user_friend2.save()
        new_user.friend.add(new_user_friend1, new_user_friend2)

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

        # Creating a new user friends
        new_user_friend1 = UserFriend(name="Arga Ghulam Ahmad", url="https://ppw-lab-arga.herokuapp.com/")
        new_user_friend2 = UserFriend(name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/")
        new_user_friend1.save()
        new_user_friend2.save()
        new_user.friend.add(new_user_friend1, new_user_friend2)

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

    def test_model_can_create_new_user_friend(self):
        # Creating a new user friends
        new_user_friend1 = UserFriend(name="Arga Ghulam Ahmad", url="https://ppw-lab-arga.herokuapp.com/")
        new_user_friend2 = UserFriend(name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/")
        new_user_friend1.save()
        new_user_friend2.save()

        # Retrieving all user friends
        counting_all_user_friends = UserFriend.objects.all().count()
        self.assertEqual(counting_all_user_friends, 2)

    def test_str_function_user(self):
        test_nama = "Arga Ghulam Ahmad"

        # Creating a new user
        new_user = User.objects.create(name=test_nama, birthday="1998-12-9", gender="M",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new user friends
        new_user_friend1 = UserFriend(name="Arga Ghulam Ahmad", url="https://ppw-lab-arga.herokuapp.com/")
        new_user_friend2 = UserFriend(name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/")
        new_user_friend1.save()
        new_user_friend2.save()
        new_user.friend.add(new_user_friend1, new_user_friend2)

        # Creating a new user expertise
        new_user_expertise1 = UserExpertise(expertise="web development")
        new_user_expertise2 = UserExpertise(expertise="mobile apps development")
        new_user_expertise1.save()
        new_user_expertise2.save()
        new_user.expertise.add(new_user_expertise1, new_user_expertise2)

        self.assertEqual(new_user.__str__(), test_nama)


    def test_str_function_user_profile(self):
        test_name = "Arga Ghulam Ahmad"

        # Creating a new user
        new_user = User.objects.create(name="Arga Ghulam Ahmad", birthday="1998-12-9", gender="M",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new user friends
        new_user_friend1 = UserFriend(name="Arga Ghulam Ahmad", url="https://ppw-lab-arga.herokuapp.com/")
        new_user_friend2 = UserFriend(name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/")
        new_user_friend1.save()
        new_user_friend2.save()
        new_user.friend.add(new_user_friend1, new_user_friend2)

        # Creating a new user expertise
        new_user_expertise1 = UserExpertise(expertise="web development")
        new_user_expertise2 = UserExpertise(expertise="mobile apps development")
        new_user_expertise1.save()
        new_user_expertise2.save()
        new_user.expertise.add(new_user_expertise1, new_user_expertise2)

        # Creating a new user profile
        new_user_profile = UserProfile.objects.create(user=new_user)

        # Creating new profile photo
        new_user_profile.photo = SimpleUploadedFile(name='test_image.jpg',
                                                    content=open('static/img/noprofile.svg', 'rb').read(),
                                                    content_type='image/jpeg')

        self.assertEqual(new_user_profile.__str__(), test_name)

    def test_str_function_user_expertise(self):
        test_expertise = "web development"

        # Creating a new user expertise
        new_user_expertise = UserExpertise.objects.create(expertise=test_expertise)

        self.assertEqual(new_user_expertise.__str__(), test_expertise)


    def test_str_function_user_post(self):
        test_name = "Arga Ghulam Ahmad"
        test_date_time = "2017-10-6 06:00:00+0800"

        # Creating a new user
        new_user = User.objects.create(name=test_name, birthday="1998-12-9", gender="M",
                                       description="a computer science student at Fasilkom UI",
                                       email="argaghulamahmad@gmail.com")

        # Creating a new user friends
        new_user_friend1 = UserFriend(name="Arga Ghulam Ahmad", url="https://ppw-lab-arga.herokuapp.com/")
        new_user_friend2 = UserFriend(name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/")
        new_user_friend1.save()
        new_user_friend2.save()
        new_user.friend.add(new_user_friend1, new_user_friend2)

        # Creating a new user expertise
        new_user_expertise1 = UserExpertise(expertise="web development")
        new_user_expertise2 = UserExpertise(expertise="mobile apps development")
        new_user_expertise1.save()
        new_user_expertise2.save()
        new_user.expertise.add(new_user_expertise1, new_user_expertise2)

        post_text = "Hai Semua! Belajar PPW Yuk :)"

        # Creating a new post
        new_post = UserPost.objects.create(user=new_user, post=post_text, date=test_date_time)

        self.assertEqual(new_post.__str__(), test_name + " " + test_date_time)


    def test_str_function_user_friend(self):
        test_name = "Arga Ghulam Ahmad"
        test_url = "https://ppw-lab-arga.herokuapp.com/"

        # Creating a new user friends
        new_user_friend = UserFriend(name=test_name, url=test_url)
        new_user_friend.save()

        self.assertEqual(new_user_friend.__str__(), test_name + " " + test_url)

    def test_set_expertise_function_user_expertise(self):
        test_expertise = "web development"

        # Creating a new user expertise
        new_user_expertise = UserExpertise.objects.create()
        new_user_expertise.setExpertise(test_expertise)
        self.assertEqual(new_user_expertise.expertise, test_expertise)

    def test_get_expertise_function_user_expertise(self):
        test_expertise = "web development"

        # Creating a new user expertise
        new_user_expertise = UserExpertise.objects.create(expertise=test_expertise)
        self.assertEqual(new_user_expertise.getExpertise(), test_expertise)

    def test_set_friend_function_user_friend(self):
        test_name = "Arga Ghulam Ahmad"
        test_url = "https://ppw-lab-arga.herokuapp.com/"

        # Creating a new user friends
        new_user_friend = UserFriend.objects.create()
        new_user_friend.setFriend(test_name, test_url)

        self.assertEqual(new_user_friend.name, test_name)

    def test_get_name_function_user_friend(self):
        test_name = "Arga Ghulam Ahmad"
        test_url = "https://ppw-lab-arga.herokuapp.com/"

        # Creating a new user friends
        new_user_friend = UserFriend.objects.create()
        new_user_friend.setFriend(test_name, test_url)

        self.assertEqual(new_user_friend.getName(), test_name)

    def test_get_url_function_user_friend(self):
        test_name = "Arga Ghulam Ahmad"
        test_url = "https://ppw-lab-arga.herokuapp.com/"

        # Creating a new user friends
        new_user_friend = UserFriend.objects.create()
        new_user_friend.setFriend(test_name, test_url)

        self.assertEqual(new_user_friend.getUrl(), test_url)