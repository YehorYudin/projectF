from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^(?P<email>.+)/user_created$', views.user_created, name='user_created')
]