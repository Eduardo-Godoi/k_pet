import itertools

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Animal, Characteristic, Group
from .serializers import AnimalSerializer


class CreateAndShowAnimal(generics.ListCreateAPIView):

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def post(self, request):
        data_animal = dict(itertools.islice(request.data.items(), 4))
        data_characteristics = request.data.pop('characteristics')
        data_group = request.data.pop('group')

        group = self.verify_group(data_group)
        animal = Animal.objects.create(**data_animal, group_id=group.id)

        animal = self.verify_characteristics(animal, data_characteristics)
        serialized = AnimalSerializer(animal)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        animals = Animal.objects.all()
        serialized = AnimalSerializer(animals, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def verify_characteristics(self, animal, characteristics):

        for item in characteristics:
            characteristic = Characteristic.objects.filter(name=item['name']).first()

            if characteristic is None:
                create = Characteristic.objects.create(name=item['name'])
                animal.characteristics.add(create)

            if characteristic:
                animal.characteristics.add(characteristic)

        return animal

    def verify_group(self, group):

        handle_group = Group.objects.filter(name=group['name']).first()

        if handle_group is None:
            return Group.objects.create(**group)

        return handle_group


class ShownAndDeleteById(generics.ListCreateAPIView):

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, animal_id=''):
        try:

            animal = Animal.objects.get(id=animal_id)
            serialized = AnimalSerializer(animal)
            return Response(serialized.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'Error': "animal id is not registered"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, animal_id=''):
        try:
            animal = Animal.objects.get(id=animal_id)
            animal.delete()
            return Response('', status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            return Response({'Error': "animal id is not registered"}, status=status.HTTP_404_NOT_FOUND)
