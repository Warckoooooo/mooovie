from django.urls import path

from . import views  # Importez la vue depuis votre module views

urlpatterns = [
    path('', views.home, name='home'),  # Définissez l'URL pour la vue home
]
