from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser

from .serializers import *
from .models import *
import json


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=serializer.data,
            status=200
        )


class CoordinatesViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = CoordinatesSerializer

    def post(self, request):
        serializer = CoordinatesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=serializer.data,
            status=200
        )


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    # parser_classes = (MultiPartParser, JSONParser)

    def get(self, request):
        serializer_for_reading = self.serializer_class(
                instance=self.queryset,
                many=True
            )
        return Response(serializer_for_reading.data)

    def post(self, request):
        image = self.serializer_class(data=request.data)
        if image.is_valid(raise_exception=True):
            image.save()
            return Response(image.data, status=200)
        else:
            return Response(status=201)


class RecordViewSet(viewsets.ViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get(self, request):
        serializer_for_reading = self.serializer_class(
                instance=self.queryset,
                many=True
            )
        return Response(serializer_for_reading.data)

    def submitData(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response({
                'status': 200,
                'message': 'Отправлено успешно',
                'id': instance.id
            }
            )

