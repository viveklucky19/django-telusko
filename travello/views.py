from django.shortcuts import render

from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "Lovely tourist city mumbai"
    dest1.img = "destination_1.jpg"
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Hyderabad"
    dest2.desc = "City of Biyani"
    dest2.img = "destination_2.jpg"
    dest2.price = 600
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Bangalore"
    dest3.desc = "Silicon Valley of INDIA"
    dest3.img = "destination_3.jpg"
    dest3.price = 800
    dest3.offer = True

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
