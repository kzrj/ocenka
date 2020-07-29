# -*- coding: utf-8 -*-
from django.test import TransactionTestCase, tag

from jobs.models import Job

import jobs.testing_utils as jobs_testing


class JobTest(TransactionTestCase):
    def setUp(self):
        jobs_testing.create_test_jobs(images=False)

    def test_create_test_jobs(self):
        self.assertEqual(Job.objects.all().count() > 0, True)


    # @tag('with_file')
    # def test_create_shop_with_product(self):
    #     category = Category.objects.all().first()
    #     image = open('../data/polufabrikati.jpg', 'rb')

