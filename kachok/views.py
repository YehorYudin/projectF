from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms

from .models import User

def index(request):
    user = User.objects.create(
        firstname="Vlad",
        lastname="Asyler",
        email="vladomar@gmail.com"
    )
    user.save()
    return HttpResponse("User created")
    #return render(request, 'core/index.html', {})

def register(request):
    return render(request, 'kachok/register.html', {})

def create_user(request):
    user = User.objects.create(
        firstname=request.POST['firstname'],
        lastname=request.POST['lastname'],
        email=request.POST['email']
    )
    user.save()
    return HttpResponseRedirect(reverse('kachok:user_created', args=(user.email,)))

def user_created(request, email):
    return render(request, 'kachok/user_created.html', {'email': email})