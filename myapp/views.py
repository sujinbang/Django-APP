from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request) :
    return render(
        request,
        "home.html",
        {}
    )

def travel(request) :
    return render(
        request,
        "travel.html",
        {}
    )