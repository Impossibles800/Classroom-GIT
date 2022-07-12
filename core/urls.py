from operator import index
from unicodedata import name
from django.core import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='setting'),
    path('upload', views.upload, name='upload')
]
