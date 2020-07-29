# -*- coding: utf-8 -*-
from rest_framework import serializers

from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    zakazchik = serializers.ReadOnlyField(source='zakazchik.profile.nickname')
    created_ago = serializers.DurationField()

    class Meta:
        model = Job
        fields = '__all__'