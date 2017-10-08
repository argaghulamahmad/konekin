from django.shortcuts import render
from main.models import *
from main.views import id_user_main

response = {}
post_set = UserPost.objects.filter(user_id=id_user_main)

def index(request):
    user = User.objects.get(id=id_user_main)
    response['username'] = user.name
    response['number_of_friends'] = user.friend.count()
    response['number_of_feeds'] = count_user_post()
    original_photo_path = UserProfile.objects.get(user_id=id_user_main).photo.url
    response['photo_path'] = original_photo_path[7:]
    response['user_post'] = reversed(post_set)
    return render(request, 'dashboard.html', response)

def count_user_post():
    total_post = 0

    for post in post_set:
        if (post.user_id==id_user_main):
            total_post += 1

    return total_post