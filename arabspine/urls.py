from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team', views.team, name="team"),
    path('faculty', views.faculty, name="faculty"),
    path('scientific_programme', views.scientific_programme, name='scientific_programme')

]