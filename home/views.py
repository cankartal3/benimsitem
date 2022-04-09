from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from bilgilerim.models import About, Projects, Educations, languages, allworks, ProjectImages
from home.models import Setting, ContactForm, ContactFormMessage


def index(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarılı bir şekilde gönderilmiştir.")
            return HttpResponseRedirect('/')

    project = Projects.objects.all()
    works = allworks.objects.all()
    language = languages.objects.all()
    education = Educations.objects.all()
    aboutme = About.objects.get()
    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting,
               'aboutme': aboutme,
               'education': education,
               'language': language,
               'works':works,
               'form': form,
               'project': project,
               'page': 'home'}
    return render(request, 'index.html', context)

    #return HttpResponse("Denemedir. %s." % text)


#def projects(request):
#    project = Projects.objects.get(pk=1)
#    context = {'project': project, 'page': 'project'}
#    return render(request, 'projects.html', context)


def references(request):
    setting = Setting.objects.get()
    context = {'setting': setting, 'page': 'references'}
    return render(request, 'references.html', context)


def project_detail(request, id, slug):
    setting = Setting.objects.get()
    project = Projects.objects.get(pk=id)
    images = ProjectImages.objects.filter(myimage_id=id)
    aboutme = About.objects.get()
    context = {
        'project': project,
        'images': images,
        'aboutme': aboutme,
        'setting': setting,
    }
    return render(request, 'projects.html', context)