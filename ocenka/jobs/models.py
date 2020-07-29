# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.core.exceptions import ValidationError as DjangoValidationError


from jobs.utils import create_resized_image_from_file

from core.models import CoreModel, CoreModelManager
from clients.models import Zakazchik, Ispolnitel


class Category(CoreModel):
    name = models.CharField(max_length=100)
    ru_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.ru_name


class JobManager(CoreModelManager):
    def create_job(self, title, category, budget, address, zakazchik, description=None, start_date=None,
     end_date=None):
    	return self.create(title=title, category=category, budget=budget, address=address,
    	 zakazchik=zakazchik, description=description, start_date=start_date, end_date=end_date)


class Job(CoreModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    budget = models.IntegerField()
    address = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    zakazchik = models.ForeignKey(Zakazchik, on_delete=models.CASCADE, related_name='jobs')
    ispolnitel = models.ForeignKey(Ispolnitel, on_delete=models.SET_NULL, null=True, related_name='jobs')

    active = models.BooleanField(default=True) 

    objects = JobManager()

    def __str__(self):
        return self.title

    @property
    def created_ago(self):
    	return (timezone.now() - self.created_at)
    


class JobImageQuerySet(models.QuerySet):
    pass


class JobImageManager(CoreModelManager):
    def get_queryset(self):
        return JobImageQuerySet(self.model, using=self._db)

    def create_job_image(self, image_file, job=None):
        job_image = self.create(job=job)
        job_pk = job.pk if job else 0
        job_image.original.save(f'{job.pk}.jpg', image_file)

        catalog_image_name = f'catalog_{job_image.original.name}'
        catalog_image = create_resized_image_from_file(image_file, 480)
        job_image.catalog_image.save(catalog_image_name, catalog_image)

        return product_image


class JobImage(CoreModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='images',
         null=True, blank=True)

    original = models.FileField(null=True, blank=True)
    catalog_image = models.FileField(null=True, blank=True)

    objects = JobImageManager()

    class Meta:
        ordering = ['pk',]


class Subscription(CoreModel):
	pass

