# -*- coding: utf-8 -*-
from django.test import TransactionTestCase, tag

from jobs.models import Job, Category
from clients.models import Profile
from subscriptions.models import ISub

import jobs.testing_utils as jobs_testing


class JobTest(TransactionTestCase):
    def setUp(self):
        jobs_testing.create_test_jobs(images=False)
        self.category1 = Category.objects.all().first()
        self.zakazchik1 = Profile.objects.filter(zakazchik=True).first()

    def test_create_test_jobs(self):
        self.assertEqual(Job.objects.all().count() > 0, True)

    @tag('with_viber')
    def test_create_job_and_mailing(self):
    	isponlitel = Profile.objects.get_or_create_profile_viber(
    		viber_id='1',
            viber_name='Test isponlitel')
    	isponlitel.mark_as_ispolnitel()
    	isub, created = ISub.objects.get_or_create(profile=isponlitel)
    	isub.categories.add(self.category1)

    	Job.objects.create_job_and_mailing(title='Test title', category=self.category1,
    		budget=100, address='test address', zakazchik=self.zakazchik1,
    		description='Test desc')


    # @tag('with_file')
    # def test_create_shop_with_product(self):
    #     category = Category.objects.all().first()
    #     image = open('../data/polufabrikati.jpg', 'rb')
