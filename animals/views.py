import pdb

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

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

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        animals = Animal.objects.all()
        serialized = AnimalSerializer(animals, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)


class GetById(generics.ListCreateAPIView):

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, id=''):
        try:

            animal = Animal.objects.get(id=id)
            serialized = AnimalSerializer(animal)
            return Response(serialized.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'Error': "animal id is not registered"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id=''):
        try:
            animal = Animal.objects.get(id=id)
            animal.delete()
            return Response('', status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            return Response({'Error': "animal id is not registered"}, status=status.HTTP_404_NOT_FOUND)


# class Delete(APIView):
#     def delete(self, request, id=''):
#         try:
#             animal = Animal.objects.delete(id=id)

#             return Response(serialized.data, status=status.HTTP_204_NO_CONTENT)
#         except ObjectDoesNotExist:
#             return Response({'Error': "animal id is not registered"}, status=status.HTTP_404_NOT_FOUND)
