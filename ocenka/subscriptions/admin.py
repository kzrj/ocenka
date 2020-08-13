from django.contrib import admin

from subscriptions.models import IspolnitelSubscription


@admin.register(IspolnitelSubscriptionofile)
class IspolnitelSubscriptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IspolnitelSubscription._meta.fields]
