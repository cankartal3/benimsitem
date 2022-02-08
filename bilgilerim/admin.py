from django.contrib import admin

# Register your models here.
from .models import About, Images

class AboutmeImageInLine(admin.TabularInline):
    model = Images
    extra = 5

class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'image', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']
    inlines = [AboutmeImageInLine]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'myimage','image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(About,AboutAdmin)
admin.site.register(Images,ImagesAdmin)
