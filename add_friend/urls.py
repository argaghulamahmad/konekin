from django.conf.urls import url
from .views import index, add_new_friend

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_new_friend/$',add_new_friend, name='add_new_friend'),
]