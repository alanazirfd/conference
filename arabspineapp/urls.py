from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('activiate/<uidb64>/<token>', views.activate, name='activate'),
    path('register', views.register, name="register"),
    path('team', views.team, name="team"),
    path('faculty', views.faculty, name="faculty"),
    path('previous_versions', views.previous_versions, name="previous_versions"),
    path('about', views.about, name="about"),
    path('sponsors', views.sponsors, name="sponsors"),
    path('scientific_programme', views.scientific_programme, name='scientific_programme')

]
