from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'team' : teams,
        'featured_cars' : featured_cars,
    }

    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'team' : teams,
    }
    return render(request, 'pages/about.html', data)
    

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')