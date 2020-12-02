from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('time2', views.time2)
]