from django.test import TestCase
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# Create your tests here.
from django.test import Client
from django.urls import resolve
from .views import index, add_status
from .forms import Status_Form

    # Create your tests here.
class UpdateStatusUnitTest(TestCase):

        def test_update_status_url_is_exist(self):
            response = Client().get('/update-status/')
            self.assertEqual(response.status_code, 200)

        def test_update_status_using_index_func(self):
            found = resolve('/update-status/')
            self.assertEqual(found.func, index)

        '''
        def test_form_input_has_placeholder_and_css_classes(self):
            form = Status_Form()
            self.assertIn('class="todo-form-input', form.as_p())
            self.assertIn('id="id_title"', form.as_p())
            self.assertIn('class="todo-form-textarea', form.as_p())
            self.assertIn('id="id_description', form.as_p())
        '''

        def test_post_success_and_render_the_result(self):
            test = 'Mantab'
            response_post = Client().post('/update-status/update-status', {'description': test})
            self.assertEqual(response_post.status_code, 302)

            response = Client().get('/update-status/')
            html_response = response.content.decode('utf8')
            self.assertIn(test, html_response)

        def test_post_error_and_render_the_result(self):
            test = 'MANTAB'
            response_post = Client().post('/update-status/update-status', { 'description': ''})
            self.assertEqual(response_post.status_code, 302)

            response = Client().get('/update-status/')
            html_response = response.content.decode('utf8')
            self.assertNotIn(test, html_response)


class UpdateStatusFunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.selenium = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(UpdateStatusFunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(UpdateStatusFunctionalTest, self).tearDown()

    def test_postarea_stastcardarea_dashboard(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/stats/')

        # find the form element
        post_area = selenium.find_element_by_id('post-area')
        stats_card_area = selenium.find_element_by_id('stats-card-area')


