# -*- coding: utf-8 -*-
import os

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from jobs.views import JobViewSet, InitTestDataView

router = routers.DefaultRouter()
router.register(r'products', JobViewSet, basename='jobs')
# router.register(r'categories', CategoryViewSet, basename='categories')
# router.register(r'shops', ShopViewSet, basename='shops')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/init_data/$', InitTestDataView.as_view()) ,    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static('/media/', document_root=os.path.join(settings.BASE_DIR, '../media'))
