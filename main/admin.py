from django.contrib import admin
from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ['series', 'amount', 'release_date', 'end_date', 'use_date', 'card_sum', 'is_active']
    list_display_links = ['series', 'amount']
    search_fields = ['series', 'amount', 'end_date', 'is_active']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'card']
    list_display_links = ['name', 'price', 'card']
    search_fields = ['name', 'price', 'card']


admin.site.register(Card, CardAdmin)
admin.site.register(Item, ItemAdmin)