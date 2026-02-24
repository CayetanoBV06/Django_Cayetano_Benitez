from django.urls import path
from . import views

urlpatterns = [
    path('',views.secciones, name="secciones"),
     path('/altas_secciones/',views.altas_secciones, name="altas_secciones"),
    path('/listado_secciones/',views.listado_secciones, name="listado_secciones"),
]