from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home),
    path('travel/', views.travel),
    path('books/', views.books)
]