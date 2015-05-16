from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^perform_login$', views.perform_login, name='perform_login'),
    url(r'^(?P<email>.+)/info$', views.user_info, name='user_info'),
    url(r'^(?P<email>.+)/user_created$', views.user_created, name='user_created')
]
