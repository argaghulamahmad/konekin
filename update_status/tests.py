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





