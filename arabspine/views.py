from django.shortcuts import render


def home(request):
    return render(request, 'main.html')


def team(request):
    return render(request, 'team.html')


def faculty(request):
    return render(request, 'faculty.html')


def sponsors(request):
    return render(request, 'sponsors.html')


def scientific_programme(request):
    return render(request, 'scientific_programme.html')

