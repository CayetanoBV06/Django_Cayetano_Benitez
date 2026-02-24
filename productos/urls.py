from django.urls import path
from . import views

urlpatterns = [
    path('',views.productos, name="productos"),
    path('/altas_productos/',views.altas_productos, name="altas_productos"),
    path('/listado_productos/',views.listado_productos, name="listado_productos"),
]