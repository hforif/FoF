from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm_list, name='farm_list'),
    path('farm/detail/<int:pk>/', views.farm_detail, name='farm_detail'),
    path('farm/create/', views.create_farm, name='create_farm'),
    path('farm/edit/<int:pk>/', views.edit_farm, name='edit_farm'),
    path('animal/', views.show_animal_list, name='show_animal_list'),
    path('animal/new/', views.add_animal, name='add_animal'),
]
