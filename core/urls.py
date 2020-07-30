from django.urls import path
from . import views

urlpatterns = [
    path('animal/', views.show_animal_list, name='show_animal_list'),
    path('animal/new/', views.add_animal, name='add_animal'),
]
