from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Add_Friend_Form
#from .models import Friend_List
from main.models import *
from main.views import id_user_main

# Create your views here.
current_user = User.objects.get(id = id_user_main)
response = {}
def index(request):
    response['add_friend'] = Add_Friend_Form
    friends = UserFriend.objects.all()
    response['friend_list'] = friends
    html = 'add_friend/add_friend.html'
    return render(request, html, response)


def add_new_friend(request):
    form = Add_Friend_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['name'] = request.POST['name']
        response['url'] = request.POST['url']        
        new_user_friend = UserFriend(name = response['name'],url = response['url'])
        new_user_friend.save()
        current_user.friend.add(new_user_friend)
        return HttpResponseRedirect('/add-friend/')
    else:
        return HttpResponseRedirect('/add-friend/')



