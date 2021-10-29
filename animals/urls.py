from django.urls import path

from .serializers import AnimalSerializer
from .views import CreateAnimal, GetById

urlpatterns = [
    path('animals/', CreateAnimal.as_view(), name='animals/'),
    path('animals/<str:id>', GetById.as_view())
]
