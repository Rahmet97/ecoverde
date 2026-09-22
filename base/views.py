from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect

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


def add_house(request):
    cities = City.objects.all()
    if request.method == "POST":
        house = House.objects.create(
            img=request.FILES['img'],
            type=request.POST['type'],
            price=request.POST['price'],
            city_id=request.POST['city'],
            address=request.POST['address'],
            description=request.POST['description'],
            room_count=request.POST['room_count'],
            floor=request.POST['floor'],
            floor_count=request.POST['floor_count'],
            area=request.POST['area'],
            title=request.POST['title'],
        )
        house.save()
        return redirect('add_house')
    return render(request, "add_house.html", {"cities": cities})
