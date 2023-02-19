from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import NGO, Message


@admin.register(NGO)
class NGO_Admin(SummernoteModelAdmin):
    """
    Controls properties of NGO table in admin panel
    """
    list_filter = ('type', 'region')
    list_display = ('name', 'pk', 'type', 'region', 'founded', 'founders', 'location', 'headquarters')
    search_fields = ['name', 'type', 'region', 'founded', 'founders', 'location', 'headquaters']
    summernote_fields = ('description',)


@admin.register(Message)
class Message_Admin(admin.ModelAdmin):
    """
    Controls properties of Message model in admin panel
    """
    list_display = ('first_name', 'last_name', 'email_address')
    search_fields = ['first_name', 'last_name', 'email_address']
