"""konekin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
import dashboard.urls as dashboard
import add_friend.urls as add_friend
import halaman_profile.urls as halaman_profile
import update_status.urls as update_status

urlpatterns = [
    url(r'^$', RedirectView.as_view(permanent=True, url='/update-status/'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^stats/', include(dashboard, namespace='dashboard')),
    url(r'^add-friend/',include(add_friend, namespace ='add-friend')),
    url(r'^halaman-profil/',include(halaman_profile, namespace='halaman_profile')),
    url(r'^update-status/',include(update_status, namespace ='update-status')),
]
