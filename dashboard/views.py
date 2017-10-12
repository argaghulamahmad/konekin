from django.shortcuts import render
from main.models import *
from main.views import id_user_main
from django.shortcuts import get_object_or_404

response = {}
post_set = UserPost.objects.filter(user_id=id_user_main)
user = get_object_or_404(User, id=id_user_main)
original_photo_path = UserProfile.objects.get(user_id=id_user_main).photo.url
username = user.name
number_of_friends = UserFriend.objects.count()
number_of_feeds = UserPost.objects.count()
photo_path = original_photo_path[7:]
reversed_post = list(reversed(post_set))

def index(request):
    response['username'] = username
    response['number_of_friends'] = number_of_friends
    response['number_of_feeds'] = number_of_feeds
    response['photo_path'] = photo_path
    response['user_post'] = reversed_post
    response['title'] = "Konekin - Stats"
    return render(request, 'dashboard.html', response)
    