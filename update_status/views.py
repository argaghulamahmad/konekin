import datetime

from django.http import HttpResponseRedirect

from dashboard.views import *
from .forms import Status_Form

# Create your views here.


response={}
new_user = User.objects.get(id=id_user_main)
now = datetime.datetime.now()

def index(request):
    post_set = UserPost.objects.filter(user_id=id_user_main)
    reversed_post = list(post_set)
    response['username'] = User.objects.first().name
    response['photo_path'] = UserProfile.objects.first().photo.url[7:]
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