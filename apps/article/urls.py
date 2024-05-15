from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('single.html', views.single),
    path('travel.html', views.travel),
    path('fashion.html', views.fashion),
]