from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bilgilerim.models import About
from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'home'}
    return render(request, 'index.html', context)

    #return HttpResponse("Denemedir. %s." % text)


def derin_ogrenme(request):
    aboutme = About.objects.get()
    context = {'aboutme': aboutme, 'page': 'derin_ogrenme'}
    return render(request, 'derin_ogrenme.html', context)
