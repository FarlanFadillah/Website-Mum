from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):

        nav_img = Food.objects.all()

        return render(request, "index.html", {'nav' : nav_img})

