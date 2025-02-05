from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('add/', views.add_film, name='add_film'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]