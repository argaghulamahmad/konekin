from django.shortcuts import render
from main.models import *
from main.views import id_user_main

response = {}

def index(request):
    response['username'] = User.objects.first().name
    response['number_of_friends'] = UserFriend.objects.count()
    response['number_of_feeds'] = UserPost.objects.count()
    response['photo_path'] = UserProfile.objects.first().photo.url[7:]
    response['user_post'] = list(reversed(UserPost.objects.filter(user_id=id_user_main)))
    response['title'] = "Konekin - Stats"
    return render(request, 'dashboard.html', response)