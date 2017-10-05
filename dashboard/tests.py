from django.test import TestCase, Client
from django.urls import resolve
from .views import index


class DashboardUnitTest(TestCase):
    # test apakah url dashboard sudah ada
    def test_dashboard_url_is_exist(self):
        response = Client().get('/stats/')
        self.assertEqual(response.status_code, 200)

    # test apakah dashboard menggunakan funcsi index() pada views dashboard
    def test_dashboard_using_index_func(self):
        found = resolve('/stats/')
        self.assertEqual(found.func, index)