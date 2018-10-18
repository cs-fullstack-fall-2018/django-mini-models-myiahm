from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.

def index(request):
    return render(request, 'apptwo/index.html')


def users(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'apptwo/users.html', context)
