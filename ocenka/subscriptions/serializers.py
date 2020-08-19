# -*- coding: utf-8 -*-
from rest_framework import serializers

from subscriptions.models import ISub
from jobs.models import Category
from jobs.serializers import CategorySerializer


class ISubSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(many=True)

    class Meta:
        model = ISub
        fields = ['categories']


class ISubCreateOrActiveSerializer(serializers.Serializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
         many=True, allow_null=True)
