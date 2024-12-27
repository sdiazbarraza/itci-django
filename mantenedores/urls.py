from django.urls import path
from . import views
from .views.index import index  # Importa la vista index desde views/index.py
from django.contrib.auth import views as auth_views  # Importa auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
    path('', index, name='index'),
    
    path('cargo/', views.cargo.cargo_list, name='cargo_list'),
    path('cargo/<int:pk>/', views.cargo.cargo_detail, name='cargo_detail'),
    path('cargo/new/', views.cargo.cargo_create, name='cargo_create'),
    path('cargo/<int:pk>/edit/', views.cargo.cargo_update, name='cargo_update'),
    path('cargo/<int:pk>/delete/', views.cargo.cargo_delete, name='cargo_delete'),

    path('producto/', views.producto.producto_list, name='producto_list'),
    path('producto/<int:pk>/', views.producto.producto_detail, name='producto_detail'),
    path('producto/new/', views.producto.producto_create, name='producto_create'),
    path('producto/<int:pk>/edit/', views.producto.producto_update, name='producto_update'),
    path('producto/<int:pk>/delete/', views.producto.producto_delete, name='producto_delete'),
]