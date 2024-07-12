
from django.urls import path

from subcategory import views

urlpatterns = [
    path('', views.read_subcategory),
    path('create/', views.create_subcategory),
    path('update/<str:pk>/', views.update_subcategory),
    path('delete/<str:pk>/', views.delete_subcategory),
]