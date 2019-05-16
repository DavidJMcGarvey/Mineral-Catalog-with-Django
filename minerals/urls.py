from django.urls import path

from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.minerals_list, name='list'),
    path('<int:pk>', views.mineral_detail, name='detail'),
    path('random/<int:pk>', views.mineral_random, name='random')
 ]
