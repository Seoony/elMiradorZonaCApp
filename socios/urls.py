from django.urls import path
from . import views

urlpatterns = [
  path('socios/', views.socios_list),
  path('socios/<int:pk>/', views.socios_detail),
  path('socios/create/', views.socios_create),
  path('socios/<int:pk>/update/', views.socios_update),
  path('socios/<int:pk>/activar/', views.activar_socio),
  path('socios/<int:pk>/desactivar/', views.desactivar_socio),
  path('socios/<int:pk>/eliminar/', views.eliminar_socio),
]