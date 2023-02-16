from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import NGO


@admin.register(NGO)
class NGO_Admin(SummernoteModelAdmin):
    """
    Controls properties of NGO table in admin panel
    """
    list_filter = ('type', 'region')
    list_display = ('name', 'pk', 'type', 'region', 'founded', 'founders', 'location', 'headquarters')
    search_fields = ['name', 'type', 'region', 'founded', 'founders', 'location', 'headquaters']
    summernote_fields = ('description',)
