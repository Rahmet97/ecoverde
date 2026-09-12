from django.shortcuts import render

from .models import House


def home(request):

    houses = House.objects.all().order_by('-created_at')

    return render(request, "index.html", {"houses": houses})


def about(request):
    return render(request, "about.html")


def agent(request):
    return render(request, "agent.html")


def services(request):
    return render(request, "services.html")
