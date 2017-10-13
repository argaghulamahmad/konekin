from django.test import TestCase, Client
from django.urls import resolve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .views import index
from main.models import *
from halaman_profile.views import *


class ProfileUnitTest(TestCase):
    #   def setUp(self):
    #      self.profile = User.objects.first()

    # test apakah url halaman-profil ada
    def test_profile_url_is_exist(self):
        response = Client().get('/halaman-profil/')
        self.assertEqual(response.status_code, 200)

    # test apakah halaman-profil menggunakan funcsi index() pada views halaman_profile
    def test_profile_using_index_func(self):
        found = resolve('/halaman-profil/')
        self.assertEqual(found.func, index)

class ProfileFunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.selenium = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(ProfileFunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(ProfileFunctionalTest, self).tearDown()

    def test_profile_picture_bio_dashboard(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/halaman-profil/')

        # find the form element
        post_area = selenium.find_element_by_id('img-profile')
        stats_card_area = selenium.find_element_by_id('bio')