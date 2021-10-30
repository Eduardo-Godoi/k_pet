from django.urls import path

from .serializers import AnimalSerializer
from .views import CreateAndShowAnimal, ShownAndDeleteById

urlpatterns = [
    path('animals/', CreateAndShowAnimal.as_view()),
    path('animals/<str:animal_id>', ShownAndDeleteById.as_view())
]
