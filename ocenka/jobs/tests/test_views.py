# -*- coding: utf-8 -*-
from datetime import datetime, date
import random

from django.contrib.auth.models import User
from django.db import connection

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from jobs.models import Job

import jobs.testing_utils as jobs_testing


class JobsViewSetTest(APITestCase):
    def setUp(self):
        jobs_testing.create_test_jobs(images=False)
        self.user1 = User.objects.get(profile__viber_name="Елена")

    def test_partial_update(self):
        self.client.force_authenticate(user=self.user1)
        job = Job.objects.filter(zakazchik=self.user1.profile).first()
        response = self.client.patch('/api/jobs/%s/' % job.pk, \
            {
                'title': 'Test',
                'budget': 100, 
                'address': 'test address', 
                'description': 'test description',
                'start_date': '2020-04-20',
            })
        self.assertEqual(response.status_code, 200)
        job.refresh_from_db()
        self.assertEqual(job.start_date, date(2020, 4, 20))
        self.assertEqual(job.title, 'Test')
        
        response = self.client.patch('/api/jobs/%s/' % job.pk, \
            {
                'title': 'Test2',
                'budget': 100, 
                'address': 'test address', 
                'description': 'test description',
                'start_date': '',
            })
        job.refresh_from_db()
        self.assertEqual(job.start_date, None)
        self.assertEqual(job.title, 'Test2')
        self.client.logout()

    def test_add_image_delete_image(self):
        self.client.force_authenticate(user=self.user1)
        job = Job.objects.filter(zakazchik=self.user1.profile).first()
        image = open('../data/dom.jpg', 'rb')
        response = self.client.post('/api/jobs/%s/add_image/' % job.pk, \
            {
                'original': image,
            })
        self.assertEqual(response.data['message'], 'Изображение добавлено.')

        job.refresh_from_db()
        image_id = job.images.all().first()
        response = self.client.post('/api/jobs/%s/delete_image/' % job.pk, \
            {
                'image': image_id.pk
            })
        self.assertEqual(response.data['message'], 'Изображение удалено.')