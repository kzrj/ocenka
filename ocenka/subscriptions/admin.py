from django.contrib import admin

from subscriptions.models import ISub


@admin.register(ISub)
class ISubAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ISub._meta.fields]
