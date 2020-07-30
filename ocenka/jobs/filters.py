# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_filters import rest_framework as filters

from jobs.models import Job, Category


class JobFilter(filters.FilterSet):
    category = filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Job
        fields = '__all__'