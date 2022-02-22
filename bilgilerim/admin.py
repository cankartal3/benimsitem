from django.contrib import admin

# Register your models here.
from .models import About, Images, Projects, Educations, languages, allworks, ProjectImages


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

class ProjectsImageInLine(admin.TabularInline):
    model = ProjectImages
    extra = 5

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['projectname']
    readonly_fields = ('image_tag',)
    inlines = [ProjectsImageInLine]

class EducationsAdmin(admin.ModelAdmin):
    list_display = ['school']

admin.site.register(About,AboutAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(Educations,EducationsAdmin)
admin.site.register(languages)
admin.site.register(allworks)


