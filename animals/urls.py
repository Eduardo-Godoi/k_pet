from django.urls import path

from .serializers import AnimalSerializer
from .views import CreateAnimal

urlpatterns = [
    path('animals/', CreateAnimal.as_view(), name='animals/')
    # path('animals/', ShowAllAnimals.as_view())
]
