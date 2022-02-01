from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text ="Django Kurulum: python -m pip install -e django <br>Proje Oluşturma: django-admin startproject mysite<br>" \
          "App ekleme: python manage.py startapp Uygulamaİsmi<br>Serverı çalıştırma: python manage.py runserver"
    context = {'text': text}  #veri ve listeler
    return render(request, 'index.html', context) # çağrılan html sayfası render edilir

    #return HttpResponse("Denemedir. %s." % text)