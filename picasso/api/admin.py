from django.contrib import admin

# Register your models here.
from .models import File


class FileAdmin(admin.ModelAdmin):
    model = File
    list_display = ('id', 'processed')


admin.site.register(File, FileAdmin)
