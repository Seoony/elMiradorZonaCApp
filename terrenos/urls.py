from django.urls import path
from . import views

urlpatterns = [
  path('terrenos/', views.list_terrenos),
  path('terrenos/<int:pk>/', views.terreno_detail),
  path('terrenos/create/', views.create_terreno),
  path('terrenos/<int:pk>/update/', views.update_terreno),
  path('terrenos/<int:pk>/activar/', views.activar_terreno),
  path('terrenos/<int:pk>/desactivar/', views.desactivar_terreno),
  path('terrenos/<int:pk>/eliminar/', views.eliminar_terreno),
]