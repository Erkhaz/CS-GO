from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return HttpResponse("CS:GO INFO")

# Create your views here.
