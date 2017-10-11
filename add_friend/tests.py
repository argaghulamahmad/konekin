from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_new_friend
# from .models import Friend_List
from .forms import Add_Friend_Form
from  main.models import *

# Create your tests here.
class AddFriendUnitTest(TestCase):

    def test_add_friend_url_is_exist(self):
        response = Client().get('/add-friend/')
        self.assertEqual(response.status_code, 200)

    # def test_add_friend_using_index_function(self):
    #     found = resolve('/add-friend/')
    #     self.assertEqual(found.func, index)

    # def test_model_can_create_new_friend(self):
    #     #Add new friend
    #     new_friend = UserFriend.objects.create(name='Dummy Makara', url = 'http://dummy.herokuapp.com')

    #     #Retrieving all friend list
    #     counting_all_friend = UserFriend.objects.all().count()
    #     self.assertEqual(counting_all_friend, 1)

    
