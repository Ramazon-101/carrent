from django.shortcuts import render, redirect
from .models import Car
from .forms import RentForm, Rent
from ..blog.models import How_it_works
from django.db.models import Q


def home_page(request):
    form = RentForm()
    wyf = form.data.get('wyf')
    wyg = form.data.get('wyg')
    j_d = form.data.get('jurney_d')
    r_d = form.data.get('return_d')
    count = Car.objects.all().count()
    hiw = How_it_works.objects.all()

    if wyf and wyg and j_d and r_d:
        cars = []
        rents = Rent.objects.filter(Q(wyf__iexact=wyf) and Q(wyg__iexact=wyg) and Q(jurney_d__exact=j_d) and Q(
            return_d__exact=r_d)).all()
        for i in rents:
            cars.append(i.car)
        context = {
            'cars': cars,
        }
        return render(request, 'cars.html', context)
    context = {
        'form': form,
        'count': count,
        'hiws': hiw,
    }
    return render(request, 'index.html', context)


def car(request):
    cars = Car.objects.all().order_by('-id')[:6]
    sd = request.POST.get('sd')
    ed = request.POST.get('ed')
    print(sd)
    print(ed)
    free_cars = Car.objects.filter(~Q(rent__jurney_d__range=[sd, ed]) or ~Q(rent__return_d__range=[sd, ed]))
    print(free_cars)
    hiw = How_it_works.objects.all()
    ctx = {
        'cars': free_cars,
        'l': [0, 1, 2, 3, 4],
        'hiws': hiw
    }
    return render(request, 'cars.html', ctx)


def rent(request, pk):
    form = RentForm(request.POST or None)
    obj = Car.objects.get(id=pk)

    if form.is_valid():
        abc = form.save(commit=False)
        abc.car = obj
        abc.save()

    context = {
        'form': form
    }
    return render(request, 'rent.html', context)
