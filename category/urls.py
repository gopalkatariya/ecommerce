
from django.urls import path

from category import views

urlpatterns = [
    path('', views.read_category),
    path('create/', views.create_category),
    path('update/<str:pk>/', views.update_category),
    path('delete/<str:pk>/', views.delete_category), 
]
