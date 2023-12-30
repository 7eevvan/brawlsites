from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_players, name='all_players'),
    path('7eevvan', views.player_7eevvan, name='player')
]