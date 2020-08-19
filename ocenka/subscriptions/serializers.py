# -*- coding: utf-8 -*-
from rest_framework import serializers

from subscriptions.models import ISub
from jobs.models import Category


class ISubSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISub
        fields = '__all__'
        # depth = 1


class ISubCreateOrActiveSerializer(serializers.Serializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
         many=True, allow_null=True)
