from django.urls import path
from . import views

urlpatterns = [
    path('cargo', views.cargo.cargo_list, name='cargo_list'),
    path('cargo/<int:pk>/', views.cargo.cargo_detail, name='cargo_detail'),
    path('cargo/new/', views.cargo.cargo_create, name='cargo_create'),
    path('cargo/<int:pk>/edit/', views.cargo.cargo_update, name='cargo_update'),
    path('cargo/<int:pk>/delete/', views.cargo.cargo_delete, name='cargo_delete'),
]