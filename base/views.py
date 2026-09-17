from django.db.models import Count
from django.shortcuts import render

from .models import House, City


def home(request):

    houses = House.objects.all().order_by('-created_at')
    cities_with_house_count = City.objects.annotate(
        house_count=Count('house')
    ).order_by('-house_count')

    return render(request, "index.html", {"houses": houses, "cities": cities_with_house_count})


def about(request):
    return render(request, "about.html")


def agent(request):
    return render(request, "agent.html")


def services(request):
    return render(request, "services.html")


def contacts(request):
    return render(request, "contact.html")
