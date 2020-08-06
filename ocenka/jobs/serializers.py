# -*- coding: utf-8 -*-
from rest_framework import serializers

from jobs.models import Job, Category


class JobSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    zakazchik = serializers.ReadOnlyField(source='zakazchik.nickname')
    created_ago = serializers.ReadOnlyField()

    class Meta:
        model = Job
        fields = '__all__'


class JobFirstCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone = serializers.IntegerField()
    start_date = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    end_date = serializers.DateTimeField(format="%Y-%m-%d", required=False)

    class Meta:
        model = Job
        fields = ['title', 'category', 'budget', 'address', 'description', 'start_date',
            'end_date', 'name', 'phone']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'modified_at']