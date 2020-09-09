# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from core.models import CoreModel, CoreModelManager


class ISubQuerySet(models.QuerySet):
    pass


class ISubManager(CoreModelManager):
    pass


class ISub(CoreModel):
    profile = models.OneToOneField('clients.Profile', on_delete=models.CASCADE,
         related_name='isub')

    categories = models.ManyToManyField('jobs.Category', related_name='isubs')

    # expired_date 

    active = models.BooleanField(default=True)  

    objects = ISubManager()

    def __str__(self):
        return f'Sub {self.profile}'
