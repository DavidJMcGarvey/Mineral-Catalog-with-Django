from django.shortcuts import render

from .models import Mineral


def minerals_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals})
