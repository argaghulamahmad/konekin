from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from main.models import *
from main.views import id_user_main
from .forms import Status_Form
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import datetime
# Create your views here.


response={}
user = User.objects.get(id=id_user_main)
now = datetime.datetime.now()
user_post = UserPost.objects.filter(user_id=id_user_main)

def index(request):
    upstatus= UserPost.objects.all()
    response['upstatus']=upstatus
    html='update-status/update-status.html'
    response['upstatus_form']=Status_Form
    UserPost.objects.create(user = user, post= response, date=now)
    return render(request, html, response)

def add_status(request):
    form = Status_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['description'] = request.POST['description']

        '''
        upstatus = UserPost(user=user, post=response['description'], date= now)
        upstatus.save()
        '''
        return HttpResponseRedirect('/update-status/')
    else:
        return HttpResponseRedirect('/update-status/')