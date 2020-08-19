# # -*- coding: utf-8 -*-
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from subscriptions.models import ISub
from subscriptions.serializers import ISubSerializer, ISubCreateOrActiveSerializer


class ISubViewSet(viewsets.ModelViewSet):
    queryset = ISub.objects.all()
    serializer_class = ISubSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return ISubCreateOrActiveSerializer
        return self.serializer_class

    def create(self, request):
        serializer = ISubCreateOrActiveSerializer(data=request.data)
        if serializer.is_valid():
            # get or create profile
            profile = request.user.profile
            isub, created = ISub.objects.get_or_create(profile=profile)
            message = ''

            if serializer.validated_data['categories']:
                isub.categories.set(serializer.validated_data['categories'])
                message = f"Подписка на {len(serializer.validated_data['categories'])} категорий"
            else:
                isub.categories.clear()
                message = 'Нет подписок.'

            return Response(
                {
                    "message": message,
                    "isub": ISubSerializer(isub).data
                },
                status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

