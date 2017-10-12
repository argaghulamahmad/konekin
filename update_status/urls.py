from django.conf.urls import url
from .views import index, add_status

urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^update-status', add_status, name='add-status'),
     
]
