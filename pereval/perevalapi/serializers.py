from django.core.exceptions import ValidationError

from .models import *
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class ImagesSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Images
        fields = ['title', 'image',]

    def create(self, validated_data):
        title = validated_data.pop('title')
        record = validated_data.pop('record')
        image = validated_data.pop('image')
        return Images.objects.create(title=title, record=record, image=image)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
       model = Users
       fields = ['email', 'first_name', 'last_name', 'father_name', 'phone']

    def create(self, validated_data):
        return Users.objects.create(**validated_data)


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude', 'height']

    def create(self, validated_data):
        return Coordinates.objects.create(**validated_data)


class RecordSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordinatesSerializer()
    image = ImagesSerializer(many=True)

    class Meta:
        model = Record
        exclude = ['status', 'id']
        include = ['image']

    def create(self, validated_data, **kwargs):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        image_data = validated_data.pop('image')

        user = Users.objects.create(**user_data)
        coords = Coordinates.objects.create(**coords_data)
        record = Record.objects.create(**validated_data, user=user, coords=coords, status="new")

        for image in image_data:
            title = image.pop('title')
            picture = image.pop('image')
            Images.objects.create(title=title, record=record, image=picture)

        return record

    def validate(self, data):
        image = data['image']
        for row in image:
            if row['image'] == None:
                raise ValidationError("Вы не прикрепили фото")

        return data





