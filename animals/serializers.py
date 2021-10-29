from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    scientific_name = serializers.CharField()


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)
