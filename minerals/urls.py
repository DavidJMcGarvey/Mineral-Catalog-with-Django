from django.urls import path

from . import views

app_name = 'minerals'

urlpatterns = [
     path('', views.minerals_list, name='list')
 ]
