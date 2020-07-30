# -*- coding: utf-8 -*-
from rest_framework import serializers

from clients.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    zakazchik = serializers.ReadOnlyField()
    ispolnitel = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['id', 'nickname', 'viber_name', 'viber_avatar', 'zakazchik', 'ispolnitel']