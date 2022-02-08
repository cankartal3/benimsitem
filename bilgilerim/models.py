from django.db import models

# Create your models here.
class Hakkımda(models.Model):
    STATUS = (
        ('True' , 'Evet'),
        ('False', 'Hayır'),
    )
    isim = models.CharField(max_length=30)
    soyisim = models.CharField(max_length=30)
    etiket = models.CharField(max_length=300)
    anahtarkelime=models.CharField(max_length=300)
    aciklama = models.CharField(max_length=300)

    ozgecmis = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True,related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.isim