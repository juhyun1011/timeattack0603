from django.http import HttpResponse
from django.shortcuts import render
from .models import DrinkModel


def coffee(request):
    if request.method == 'GET':
        return render(request, 'coffee.html')

    elif request.method == 'POST':
        coffees = request.POST.get("category")
        current_coffees = DrinkModel.objects.get(category=coffees)

        return render(request, 'coffee.html', current_coffees)
