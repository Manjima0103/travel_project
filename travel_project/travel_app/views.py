
from django.shortcuts import render, redirect
from .models import Place
from .models import Team
from .models import Pic


def demo(request):
    obj = Place.objects.all()
    obje = Team.objects.all()
    objec = Pic.objects.all()

    return render(request, "index.html", {'result': obj, 'results': obje, 'res': objec})


