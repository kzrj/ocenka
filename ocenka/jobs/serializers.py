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
    # ! allow_null doesnt work without default
    start_date = serializers.DateField(format="%Y-%m-%d", allow_null=True, default=None)
    end_date = serializers.DateField(format="%Y-%m-%d", allow_null=True, default=None)

    class Meta:
        model = Job
        fields = ['title',
            'category', 'budget', 'address', 'description',
            'start_date',
            'end_date', 
            'name',
            'phone',
            ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'modified_at']