import pdb

from rest_framework import generics
from rest_framework.response import Response

from .models import Animal, Characteristic, Group
from .serializers import AnimalSerializer


class CreateAnimal(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def post(self, request):
        data = request.data
        name, age, weight, sex, group, characteristics = data.values()

        create_group = Group.objects.create(name=group['name'], scientific_name=group['scientific_name'])

        animal = Animal.objects.create(name=name, age=age, weight=weight, sex=sex, group_id=create_group.id)

        for item in characteristics:
            c = Characteristic.objects.create(name=item['name'])
            animal.characteristics.add(c)

        serialized = AnimalSerializer(animal)

        return Response(serialized.data)

    def get(self, request):
        animals = Animal.objects.all()
        serialized = AnimalSerializer(animals, many=True)

        return Response(serialized.data)
