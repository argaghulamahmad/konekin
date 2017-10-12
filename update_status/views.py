from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import *
from main.views import id_user_main
from .forms import Status_Form
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import datetime
# Create your views here.


response={}
user = get_object_or_404(User, id=id_user_main)
username = user.name
new_user = User.objects.get(id=id_user_main)
now = datetime.datetime.now()
#post_set = UserPost.objects.filter(user_id=id_user_main)
postingan =UserPost.objects.all().values()
original_photo_path = UserProfile.objects.get(user_id=id_user_main).photo.url
photo_path = original_photo_path[7:]


def index(request):
    post_set = UserPost.objects.filter(user_id=id_user_main)
    reversed_post = list(post_set)
    response['username'] = username
    response['photo_path'] = photo_path
    response['user_post'] = post_set
    response['title'] = "Konekin - Update Status"
    response['upstatus_form'] = Status_Form
    return render(request, 'update-status.html', response)

def add_status(request):
    form = Status_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['description'] = request.POST['description']
        todo = UserPost(user = new_user, post = response['description'], date=now)
        todo.save()
        return HttpResponseRedirect('/update-status/')
    else:
        return HttpResponseRedirect('/update-status/')