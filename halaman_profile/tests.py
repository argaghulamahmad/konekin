from django.test import TestCase, Client
from django.urls import resolve
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
