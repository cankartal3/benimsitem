from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status']

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'status', 'note', 'ip']
    list_filter = ['status']

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)