from django.test import TestCase, Client
from django.urls import resolve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from dashboard.views import index
from main.models import *


class DashboardUnitTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Arga Ghulam Ahmad", birthday="1998-12-9", gender="M",
            description="a computer science student at Fasilkom UI",
            email="argaghulamahmad@gmail.com"
        )

        UserPost.objects.create(
            user=self.user, post="Hai Semua! Belajar PPW Yuk :)", date="2017-10-6 06:00:00+0800"
        )

        UserFriend.objects.create(
            name="Claudio Yosafat", url="https://ppw-lab-claudio.herokuapp.com/", date="2017-10-6 06:00:00+0800"
        )

        UserProfile.objects.create(
            user=self.user
        )


    # test apakah url dashboard sudah ada
    def test_dashboard_url_is_exist(self):
        response = Client().get('/stats')
        self.assertEqual(response.status_code, 301)

    # test apakah dashboard menggunakan funcsi index() pada views dashboard
    def test_dashboard_using_index_func(self):
        found = resolve('/stats/')
        self.assertEqual(found.func, index)

    def test_stats_display_correct_total_post_and_friend(self):
        response = Client().get('/stats/')
        html_response = response.content.decode('utf8')
        self.assertIn(str(self.user.friend.count()), html_response)
        self.assertIn(str(UserPost.objects.count()), html_response)

    #def test_stats_show_latest_post(self):
    #    response = Client().get('/stats/')
    #    html_response = response.content.decode('utf8')
    #    self.assertIn(str(UserPost.objects.first().post), html_response)

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

    def test_postarea_stastcardarea_dashboard(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/stats/')

        # find the form element
        post_area = selenium.find_element_by_id('post-area')
        stats_card_area = selenium.find_element_by_id('stats-card-area')
