from django.test import TestCase, Client
from django.urls import resolve
from .views import index
from main.models import *
from dashboard.views import count_user_post

class DashboardUnitTest(TestCase):
    # test apakah url dashboard sudah ada
    def test_dashboard_url_is_exist(self):
        response = Client().get('/stats/')
        self.assertEqual(response.status_code, 200)

    # test apakah dashboard menggunakan funcsi index() pada views dashboard
    def test_dashboard_using_index_func(self):
        found = resolve('/stats/')
        self.assertEqual(found.func, index)

    # test apakan fungsi count_user_post() valid
    def test_count_user_post(self):
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

        total_post = count_user_post()
        self.assertEqual(total_post, 1)
