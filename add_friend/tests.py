from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_new_friend
# from .models import Friend_List
from .forms import Add_Friend_Form
from  main.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Create your tests here.
class AddFriendUnitTest(TestCase):

    def test_add_friend_url_is_exist(self):
        response = Client().get('/add-friend/')
        self.assertEqual(response.status_code, 200)

    def test_using_index_function(self):
        found = resolve('/add-friend/')
        self.assertEqual(found.func, index)

    def test_using_add_new_friend_function(self):
        found = resolve('/add-friend/add_new_friend/')
        self.assertEqual(found.func, add_new_friend)

    def test_model_can_create_new_friend(self):
        new_friend = UserFriend.objects.create(name='Dummy Makara', url = 'http://dummy.herokuapp.com')

        counting_all_friend = UserFriend.objects.all().count()
        self.assertEqual(counting_all_friend, 1)

    def test_add_new_friend_success_and_render_the_result(self):
        name = 'Dummy'
        url = 'http://dummy.herokuapp.com'
        response = Client().post('/add-friend/add_new_friend/', {'name': name, 'url': url})
        self.assertEqual(response.status_code, 302)
        response = Client().get('/add-friend/')
        html_response = response.content.decode('utf8')
        self.assertIn(name,html_response)
        self.assertIn(url,html_response)

    def test_add_friend_showing_all_friend(self):
        name_dummy = 'Dummy'
        url_dummy = 'http://dummy.herokuapp.com'
        friend_dummy = {'name' : name_dummy, 'url' : url_dummy}
        add_new_friend_dummy = Client().post('/add-friend/add_new_friend/',friend_dummy)
        self.assertEqual(add_new_friend_dummy.status_code, 302)

        name_dio = 'Dio'
        url_dio = 'http://dio.herokuapp.com'
        friend_dio = {'name' :  name_dio, 'url' : url_dio}
        add_new_friend_dio = Client().post('/add-friend/add_new_friend/',friend_dio)
        self.assertEqual(add_new_friend_dio.status_code, 302)

        response = Client().get('/add-friend/')
        html_response = response.content.decode('utf8')

        self.assertIn(name_dummy,html_response)
        self.assertIn(url_dummy, html_response)
        self.assertIn(name_dio, html_response)
        self.assertIn(url_dio, html_response)


    def test_add_new_friend_fail(self):
        response = Client().post('/add-friend/add_new_friend/',{'name' : 'Dummy', 'url' : 'dummy'})
        self.assertEqual(response.status_code, 302)

    def test_add_friend_form_validation_for_blank_items(self):
        form = Add_Friend_Form(data={'name': '', 'url': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'],["This field is required."])
        self.assertEqual(form.errors['url'],["This field is required."])

    
class AddFriendFunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')        
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(AddFriendFunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AddFriendFunctionalTest, self).tearDown()

    def test_add_new_friend(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/add-friend/')
        name = selenium.find_element_by_id('id_name')
        url = selenium.find_element_by_id('id_url')
        add_friend = selenium.find_element_by_id('btn')
        name.send_keys('Dummy')
        url.send_keys('http://dummy.herokuapp.com')
        add_friend.send_keys(Keys.RETURN)