from django.contrib import admin

from jobs.models import Category, Job


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Job._meta.fields]