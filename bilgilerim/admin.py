from django.contrib import admin

# Register your models here.
from .models import Hakkımda
class HakkımdaAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'status']
    list_filter = ['status']

admin.site.register(Hakkımda,HakkımdaAdmin)