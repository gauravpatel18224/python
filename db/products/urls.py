from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('product/<int:pk>/update/', views.update_product, name='update_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('subcategory/add/', views.add_subcategory, name='add_subcategory'),
    path('subcategory/<int:pk>/update/', views.update_subcategory, name='update_subcategory'),
    path('subcategory/<int:pk>/delete/', views.delete_subcategory, name='delete_subcategory'),
]
