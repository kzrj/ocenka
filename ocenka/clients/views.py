# # -*- coding: utf-8 -*-
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from clients.models import Profile
from clients.serializers import ProfileUpdateSerializer, ProfileSerializer

from core.permissions import ObjAndOwnerPermissions


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [ObjAndOwnerPermissions]

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return ProfileUpdateSerializer
        return self.serializer_class

    def create(self, request):
    	pass

    def retrieve(self, request, pk=None):
    	pass

    def destroy(self, request, pk=None):
    	pass

