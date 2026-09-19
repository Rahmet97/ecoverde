from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render

from .models import House, City


def home(request):

    houses = House.objects.all().order_by('-created_at')
    cities_with_house_count = City.objects.annotate(
        house_count=Count('house')
    ).order_by('-house_count')
    agents = User.objects.filter(is_staff=True, is_superuser=False)

    return render(
        request,
        "index.html",
        {
            "houses": houses,
            "cities": cities_with_house_count,
            "agents": agents,
        }
    )


def about(request):
    return render(request, "about.html")


def agent(request):
    agents = User.objects.filter(is_staff=True)
    return render(request, "agent.html", {"agents": agents})


def services(request):
    return render(request, "services.html")


def contacts(request):
    return render(request, "contact.html")
