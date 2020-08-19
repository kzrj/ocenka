# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from subscriptions.models import ISub

import jobs.testing_utils as jobs_testing


class ISubViewSetTest(APITestCase):
    def setUp(self):
        jobs_testing.create_test_jobs(images=False)
        self.user1 = User.objects.get(profile__viber_name="Елена")

    def test_partial_update(self):
        self.client.force_authenticate(user=self.user1)
        
        response = self.client.post('/api/subs/', \
            {
                'categories': [1,2,3],
            })
        self.assertEqual('Подписка на' in response.data['message'], True)

        response = self.client.post('/api/subs/', \
            {
                'categories': [],
            })
        self.assertEqual('Нет подписок' in response.data['message'], True)
