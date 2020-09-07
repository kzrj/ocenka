# -*- coding: utf-8 -*-
from rest_framework import serializers

from jobs.models import Job, Category, JobImage


class JobImageSerializer(serializers.ModelSerializer):
    catalog_image = serializers.ReadOnlyField(source='catalog_image.url')
    thumb_image = serializers.ReadOnlyField(source='thumb_image.url')
    non_zoom_image = serializers.ReadOnlyField(source='non_zoom_image.url')

    class Meta:
        model = JobImage
        fields = ['catalog_image', 'thumb_image', 'non_zoom_image', 'id']


class JobImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobImage
        fields = ['original']


class JobImageIdSerializer(serializers.Serializer):
    image = serializers.PrimaryKeyRelatedField(queryset=JobImage.objects.all())


class JobSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    zakazchik = serializers.ReadOnlyField(source='zakazchik.nickname')
    created_ago = serializers.ReadOnlyField()
    images = JobImageSerializer(many=True)

    class Meta:
        model = Job
        fields = '__all__'


class JobFullSerializer(JobSerializer):
    zakazchik_phone = serializers.ReadOnlyField(source='zakazchik.phone')
    

class JobFirstCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone = serializers.IntegerField()
    # ! allow_null doesnt work without default
    start_date = serializers.DateField(format="%Y-%m-%d", allow_null=True, default=None)
    end_date = serializers.DateField(format="%Y-%m-%d", allow_null=True, default=None)

    class Meta:
        model = Job
        fields = [
            'title',
            'category', 
            'budget', 
            'address', 
            'description',
            'start_date',
            'end_date', 
            'name',
            'phone',
            ]


class JobUpdateSerializer(serializers.ModelSerializer):
    # ! allow_null doesnt work without default
    start_date = serializers.DateField(format="%Y-%m-%d", allow_null=True, default=None)
    end_date = serializers.DateField(format="%Y-%m-%d", allow_null=True, default=None)

    class Meta:
        model = Job
        fields = [
            'title',
            'category', 
            'budget', 
            'address', 
            'description',
            'start_date',
            'end_date', 
            ]


class JobDeactivateSerializer(serializers.Serializer):
    active = serializers.BooleanField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'modified_at']