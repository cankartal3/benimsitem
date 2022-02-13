from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

import bilgilerim.models


class About(models.Model):
    STATUS = (
        ('True' , 'Evet'),
        ('False', 'Hayır'),
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    title = models.CharField(max_length=300)
    keywords = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    job = models.CharField(max_length=50)
    personal_background = RichTextUploadingField()
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True,related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))
        else:
            return mark_safe('<img src="{}" height="100"/>'.format("/uploads/images/resim-yok.png"))

    image_tag.short_description = 'Image'
class Images(models.Model):
    myimage = models.ForeignKey(About, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


    def image_tag(self): # Burada resim olmayanlar için çözüm üretilmiştir.
        if self.image: # Resim adresi varsa. Yani resim varsa.
            return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))
        else:          # # Resim adresi yoksa. Yani resim yoksa.
            return mark_safe('<img src="{}" height="100"/>'.format("/uploads/images/resim-yok.png"))
    image_tag.short_description = 'Image'

class Projects(models.Model):
    projectowner = models.ForeignKey(About, on_delete=models.CASCADE)
    projectname = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    contentofproject = RichTextUploadingField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)





