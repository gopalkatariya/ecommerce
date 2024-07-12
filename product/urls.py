
from django.urls import path

from product import views

urlpatterns = [
    path('product/', views.read_product),
    path('product/create/', views.create_product),
    path('product/update/<str:pk>/', views.update_product),
    path('product/delete/<str:pk>/', views.delete_product),

    path('category/', views.read_category),
    path('category/create/', views.create_category),
    path('category/update/<str:pk>/', views.update_category),
    path('category/delete/<str:pk>/', views.delete_category),
    
    path('subcategory/', views.read_subcategory),
    path('subcategory/create/', views.create_subcategory),
    path('subcategory/update/<str:pk>/', views.update_subcategory),
    path('subcategory/delete/<str:pk>/', views.delete_subcategory),
]