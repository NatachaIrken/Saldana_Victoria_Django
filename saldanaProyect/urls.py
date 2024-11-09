"""
URL configuration for saldanaProyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto_APP import views

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', views.index, name='index'), 
#    path('', views.listaPersona, name='listar_personas'),  
#    path('agregar/', views.agregarPersona, name='agregar_persona'), 
#    path('listarP/', views.listaPersona, name='listar_personas'),  
#    path('eliminar/<int:id>/', views.eliminarPersona, name='eliminar_persona'),
#    path('actualizar/<int:id>/', views.actualizarPersona, name='actualizar_persona'),
#]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('agregar/', views.agregarPersona, name='agregar_persona'),
    path('listarP/', views.listaPersona, name='listar_personas'),
    path('eliminarP/<int:id>/', views.eliminarPersona, name='eliminar_persona'),  
    path('actualizarP/<int:id>/', views.actualizarPersona, name='actualizar_persona'), 
]
