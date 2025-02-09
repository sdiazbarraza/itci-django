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

    path('centro/', views.centro.centro_list, name='centro_list'),
    path('centro/<int:pk>/', views.centro.centro_detail, name='centro_detail'),
    path('centro/new/', views.centro.centro_create, name='centro_create'),
    path('centro/<int:pk>/edit/', views.centro.centro_update, name='centro_update'),
    path('centro/<int:pk>/delete/', views.centro.centro_delete, name='centro_delete'),

    path('causa_raiz/', views.causa_raiz.causa_raiz_list, name='causa_raiz_list'),
    path('causa_raiz/<int:pk>/', views.causa_raiz.causa_raiz_detail, name='causa_raiz_detail'),
    path('causa_raiz/new/', views.causa_raiz.causa_raiz_create, name='causa_raiz_create'),
    path('causa_raiz/<int:pk>/edit/', views.causa_raiz.causa_raiz_update, name='causa_raiz_update'),
    path('causa_raiz/<int:pk>/delete/', views.causa_raiz.causa_raiz_delete, name='causa_raiz_delete'),

    path('puesto_trabajo/', views.puesto_trabajo.puesto_trabajo_list, name='puesto_trabajo_list'),
    path('puesto_trabajo/<int:pk>/', views.puesto_trabajo.puesto_trabajo_detail, name='puesto_trabajo_detail'),
    path('puesto_trabajo/new/', views.puesto_trabajo.puesto_trabajo_create, name='puesto_trabajo_create'),
    path('puesto_trabajo/<int:pk>/edit/', views.puesto_trabajo.puesto_trabajo_update, name='puesto_trabajo_update'),
    path('puesto_trabajo/<int:pk>/delete/', views.puesto_trabajo.puesto_trabajo_delete, name='puesto_trabajo_delete'),

    path('tipo_merma/', views.tipo_merma.tipo_merma_list, name='tipo_merma_list'),
    path('tipo_merma/<int:pk>/', views.tipo_merma.tipo_merma_detail, name='tipo_merma_detail'),
    path('tipo_merma/new/', views.tipo_merma.tipo_merma_create, name='tipo_merma_create'),
    path('tipo_merma/<int:pk>/edit/', views.tipo_merma.tipo_merma_update, name='tipo_merma_update'),
    path('tipo_merma/<int:pk>/delete/', views.tipo_merma.tipo_merma_delete, name='tipo_merma_delete'),

    path('unidad_medida/', views.unidad_medida.unidad_medida_list, name='unidad_medida_list'),
    path('unidad_medida/<int:pk>/', views.unidad_medida.unidad_medida_detail, name='unidad_medida_detail'),
    path('unidad_medida/new/', views.unidad_medida.unidad_medida_create, name='unidad_medida_create'),
    path('unidad_medida/<int:pk>/edit/', views.unidad_medida.unidad_medida_update, name='unidad_medida_update'),
    path('unidad_medida/<int:pk>/delete/', views.unidad_medida.unidad_medida_delete, name='unidad_medida_delete'),

    path('turno/', views.turno.turno_list, name='turno_list'),
    path('turno/<int:pk>/', views.turno.turno_detail, name='turno_detail'),
    path('turno/new/', views.turno.turno_create, name='turno_create'),
    path('turno/<int:pk>/edit/', views.turno.turno_update, name='turno_update'),
    path('turno/<int:pk>/delete/', views.turno.turno_delete, name='turno_delete'), 

    path('colaborador/', views.colaborador.colaborador_list, name='colaborador_list'),
    path('colaborador/<int:pk>/', views.colaborador.colaborador_detail, name='colaborador_detail'),
    path('colaborador/new/', views.colaborador.colaborador_create, name='colaborador_create'),
    path('colaborador/<int:pk>/edit/', views.colaborador.colaborador_update, name='colaborador_update'),
    path('colaborador/<int:pk>/delete/', views.colaborador.colaborador_delete, name='colaborador_delete'), 

    path('merma/', views.merma.merma_list, name='merma_list'),
    path('merma/<int:pk>/', views.merma.merma_detail, name='merma_detail'),
    path('merma/new/', views.merma.merma_create, name='merma_create'),
    path('merma/<int:pk>/edit/', views.merma.merma_update, name='merma_update'),
    path('merma/<int:pk>/delete/', views.merma.merma_delete, name='merma_delete'),        
]