from django.contrib import admin
from django.urls import path
from .views import pokemon, trainer

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_view'),
    path('pokemon/', pokemon, name='pokemon_view'),
    path('trainer/', trainer, name='trainer_view'),
]
