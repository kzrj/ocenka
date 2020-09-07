# -*- coding: utf-8 -*-
from rest_framework import serializers

from clients.models import Profile
from subscriptions.serializers import  ISubSerializer


class ProfileSerializer(serializers.ModelSerializer):
    isub = ISubSerializer(allow_null=True)

    class Meta:
        model = Profile
        fields = ['id', 'nickname', 'viber_name', 'viber_avatar', 'zakazchik', 'phone',
             'ispolnitel', 'isub']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname', 'phone']
        