from django.contrib import admin
from .models import ArtImage

class ArtImageAdmin(admin.ModelAdmin):
    list_display=['name','uploaded_at']

admin.site.register(ArtImage, ArtImageAdmin)
