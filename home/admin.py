from django.contrib import admin

# Register your models here.
from home.models import Setting

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status']

admin.site.register(Setting,SettingAdmin)