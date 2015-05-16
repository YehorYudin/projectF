from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms

from .models import User


def get_obj_or_404(klass, *args, **kwargs):
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        raise Http404

def index(request):
    return HttpResponse("Hi")

def register(request):
    return render(request, 'kachok/register.html', {})

def create_user(request):
    user = User.objects.create(
        firstname=request.POST['firstname'],
        lastname=request.POST['lastname'],
        email=request.POST['email'],
        password=request.POST['password']
    )
    user.save()
    return HttpResponseRedirect(reverse('kachok:user_created', args=(user.email,)))

def user_created(request, email):
    return render(request, 'kachok/user_created.html', {'email': email})

def login(request):
    return render(request, 'kachok/login.html', {})

def perform_login(request):
    try:
        user = User.objects.get(
            email=request.POST['email'],
            password=request.POST['password']
        )
    except User.DoesNotExist:
        return render(request, 'kachok/login.html', {
            'error_message': "Login/password mistmatch.",
        })
    else:
        return HttpResponseRedirect(reverse('kachok:user_info', args=(user.email,)))

def user_info(request, email):
    user = get_obj_or_404(User, email=email)
    return render(request, 'kachok/info.html', {'user': user})
