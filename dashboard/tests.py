from django.test import TestCase, Client
from django.urls import resolve

from dashboard.views import count_user_post, index, username, number_of_friends, number_of_feeds, photo_path, \
    reversed_post, response
from main.models import User, UserPost, UserExpertise, UserFriend


class DashboardUnitTest(TestCase):
    # test apakah url dashboard sudah ada
    def test_dashboard_url_is_exist(self):
        response = Client().get('/stats')
        self.assertEqual(response.status_code, 301)

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
        self.assertEqual(total_post, 3)

    # def test_response_username(self):
    #     response = Client().get('/stats')
    #     self.assertEqual(username, response['username'])
    #
    # def test_response_user_of_friends(self):
    #     response = Client().get('/stats')
    #     self.assertEqual(number_of_friends, response['number_of_friends'])
    #
    # def test_response_user_of_feeds(self):
    #     response = Client().get('/stats')
    #     self.assertEqual(number_of_feeds, response['number_of_feeds'])
    #
    # def test_response_photo_path(self):
    #     response = Client().get('/stats')
    #     self.assertEqual(photo_path, response['photo_path'])
    #
    # def test_response_user_post(self):
    #     response = Client().get('/stats')
    #     self.assertEqual(reversed_post, response['user_post'])

    # def test_dashboard_information(self):
    #     response = Client().get('/stats')
    #     self.assertEqual(response['username'], username)
    #     self.assertEqual(response['number_of_friends'], number_of_friends)
    #     self.assertEqual(response['number_of_feeds'], number_of_feeds)
    #     self.assertEqual(response['photo_path'], photo_path)
    #     self.assertEqual(response['user_post'], reversed_post)