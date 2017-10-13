from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import resolve
from .views import index, add_status
from .models import UpStatus
from .forms import Status_Form

    # Create your tests here.
class UpdateStatusUnitTest(TestCase):

		def test_update_status_url_is_exist(self):
			response = Client().get('/update-status/')
			self.assertEqual(response.status_code, 200)

		def test_update_status_using_index_func(self):
			found = resolve('/update-status/')
			self.assertEqual(found.func, index)

		def test_model_can_create_update_status(self):
			# Creating a new activity
			new_activity = UpStatus.objects.create( description='mengerjakan  ppw')

			# Retrieving all available activity
			counting_all_available_upsatus = UpStatus.objects.all().count()
			self.assertEqual(counting_all_available_upsatus, 1)

