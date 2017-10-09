from django.test import TestCase, Client
from django.urls import resolve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from dashboard.views import count_user_post, index, username, number_of_friends, number_of_feeds, reversed_post, \
    original_photo_path
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
        new_post = UserPost.objects.create(user=new_user, post=post_text, date="2017-10-6 06:00:00+0700")

        total_post = count_user_post()
        self.assertEqual(total_post, 3)

    def test_dashboard_information(self):
        response = Client().get('/stats/')
        html_response = response.content.decode('utf8')
        photo_path = original_photo_path[:27]
        self.assertIn(username, html_response)
        self.assertIn(str(number_of_friends), html_response)
        self.assertIn(str(number_of_feeds), html_response)
        self.assertIn(photo_path, html_response)

class DashboardFunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.selenium = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(DashboardFunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(DashboardFunctionalTest, self).tearDown()

    def test_dashboard(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/stats/')

        # find the form element
        selenium.find_element_by_id('post-area')
        selenium.find_element_by_id('stats-card-area')
