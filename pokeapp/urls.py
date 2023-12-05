from django.contrib import admin
from django.urls import path
from pokeapp import views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin_view'),
    path('', views.pokemon, name='pokemon_view'),
    path('trainer/', views.trainer, name='trainer_view'),
    path('collection/', views.collection, name='collection_view'),
]
