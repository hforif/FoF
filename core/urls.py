from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm_list, name='farm_list'),
    path('farm/<int:pk>/detail', views.farm_detail, name='farm_detail'),
    path('farm/create/', views.create_farm, name='create_farm'),
    path('farm/<int:pk>/edit/', views.edit_farm, name='edit_farm'),
]
