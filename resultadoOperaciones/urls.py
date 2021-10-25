from django.urls import path

from resultadoOperaciones import views


urlpatterns = [
    path('resultado/', views.Resultados.as_view())
]
