import json

from django.contrib.auth.models import User, AnonymousUser
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from .models import House, City, Basket


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


def properties(request):
    if request.method == 'POST':
        house_id = request.POST.get('house_id')
        user = request.user
        if isinstance(user, AnonymousUser):
            return redirect('login')
        basket = Basket.objects.create(house_id=house_id, user_id=user.id)
        basket.save()


    q = request.GET.get('q')
    apartment_type = request.GET.get('type')
    city_id = request.GET.get('city_id')
    price_from = float(request.GET.get('price_from') or 0)
    price_to = float(request.GET.get('price_to') or 0)
    houses = House.objects.all()
    cities = City.objects.all()
    if q:
        houses = houses.filter(
            Q(title__icontains=q) | Q(city__name__icontains=q)
        )
    if apartment_type:
        houses = houses.filter(type=apartment_type.capitalize())
    if city_id:
        houses = houses.filter(city_id=city_id)
    if price_from:
        houses = houses.filter(price__gte=price_from)
    if price_to:
        houses = houses.filter(price__lte=price_to)
    houses = houses.order_by('-created_at')
    return render(request, "properties.html", {"houses": houses, "cities": cities})


def property_details(request, pk):
    house = House.objects.get(pk=pk)
    return render(request, "properties-single.html", {"house": house})


class HouseView(TemplateView):
    template_name = "add_house.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cities = City.objects.all()

        context['cities'] = cities
        return context

    def post(self, request, *args, **kwargs):
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
            broker=request.user,
        )
        house.save()
        return redirect('add_house')


class BasketView(TemplateView):
    template_name = 'basket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.request.user.is_anonymous:
        #     return redirect('login')
        basket = Basket.objects.filter(user_id=self.request.user.id)
        context['basket'] = basket
        return context


@require_POST
def update_count(request):
    count = json.loads(request.body).get('count')
    basket_id = json.loads(request.body).get('basket_id')

    basket = Basket.objects.get(id=basket_id)
    basket.count += count
    basket.save()
    return JsonResponse({"message": "Count updated successfully"})
