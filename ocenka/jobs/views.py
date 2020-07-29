# # -*- coding: utf-8 -*-
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from jobs.models import Job
from jobs.serializers import JobSerializer
from jobs.testing_utils import create_test_jobs


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class InitTestDataView(APIView):
    def get(self, request, format=None):
        create_test_jobs()
        return Response({'msg': 'Done.'})