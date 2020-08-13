# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from core.models import CoreModel, CoreModelManager


class IspolnitelSubscriptionQuerySet(models.QuerySet):
    pass


class IspolnitelSubscriptionManager(CoreModelManager):
    pass


class IspolnitelSubscription(CoreModel):
    profile = models.OneToOneField('clients.Profile', on_delete=models.SET_NULL, null=True, 
        related_name='isub')

    categories = models.ManyToManyField('jobs.Category', related_name='isubs')

    # expired_date 

    active = models.BooleanField(default=True)  

    objects = IspolnitelSubscriptionManager()

    def __str__(self):
        return f'Sub {self.profile.nickname}'
