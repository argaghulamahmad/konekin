from django.test import TestCase, Client
from django.urls import resolve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from dashboard.views import index, username, number_of_friends, number_of_feeds, original_photo_path


class DashboardUnitTest(TestCase):
    # test apakah url dashboard sudah ada
    def test_dashboard_url_is_exist(self):
        response = Client().get('/stats')
        self.assertEqual(response.status_code, 301)

    # test apakah dashboard menggunakan funcsi index() pada views dashboard
    def test_dashboard_using_index_func(self):
        found = resolve('/stats/')
        self.assertEqual(found.func, index)

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

    def test_postarea_stastcardarea_dashboard(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/stats/')

        # find the form element
        post_area = selenium.find_element_by_id('post-area')
        stats_card_area = selenium.find_element_by_id('stats-card-area')