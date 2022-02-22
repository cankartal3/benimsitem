from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(blank=True, max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=35)
    smtpemail = models.CharField(blank=True, max_length=35)
    smtppassword = models.CharField(blank=True, max_length=40)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    linkedin = models.CharField(blank=True, max_length=60)
    aboutme = RichTextUploadingField()
    contact = models.TextField(blank=True, )
    references = models.TextField(blank=True, )
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.icon:
            return mark_safe('<img src="{}" height="100"/>'.format(self.icon.url))
        else:
            return mark_safe('<img src="{}" height="100"/>'.format("/uploads/images/resim-yok.png"))

    image_tag.short_description = 'Site icon'

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Read', 'Okundu'),
        ('Closed', 'Kapandı'),
    )
    email = models.CharField(blank=True, max_length=100)
    subject = models.CharField(blank=True, max_length=100)
    message = models.TextField(blank=True, max_length=200)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['email', 'subject', 'message']
        widgets = {
            'email'     : TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'subject'   : TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
            'message'   : Textarea(attrs={'class': 'form-control', 'placeholder': 'message', 'rows': '5'}),
        }
