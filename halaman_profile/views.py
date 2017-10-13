from django.shortcuts import render
from main.models import *
from main.views import id_user_main
from django.shortcuts import get_object_or_404
# Create your views here.

response = {}
user = get_object_or_404(User, id=id_user_main)
original_photo_path = UserProfile.objects.get(user_id=id_user_main).photo.url
photo_path = original_photo_path[7:]

def index(request):

    response['profile_pic'] = photo_path
    response['name'] = user.name
    response['birthday'] = user.birthday
    response['gender'] = user.get_gender_display()
    response['expertise'] = user.expertise.all()
    response['description'] = user.description
    response['email'] = user.email
    response['title'] = "Konekin - Profile"

    html = "profile.html"

    return render(request, html, response)
