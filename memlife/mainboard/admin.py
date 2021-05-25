from django.contrib import admin
from .models import Mem

class MemAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'mem', 'created', 'user']
    list_filter = ['created']

admin.site.register(Mem, MemAdmin)