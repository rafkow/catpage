from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import models
from datetime import datetime
from random import sample, choice


def index(request):
    template = loader.get_template("home.html")
    about_pictures = models.Gallery.objects.order_by('?')[:4]
    citation = models.Citation.objects.order_by('?').first()
    print(citation.name)
    context = {
        'about_pictures': about_pictures,
        'citation': citation
    }
    return render(request, 'home.html', context)


def koty(request):
    template = loader.get_template("koty.html")
    all = models.CatProfile.objects.filter(display=True)
    cats = all.filter(sex='1,0')
    kitten = all.filter(sex='0,1')
    context = {
        'cats': cats,
        'kitten': kitten,
    }
    return HttpResponse(template.render(context, request))


def mioty(request):
    template = loader.get_template("mioty.html")
    # excepted_litters = models.Litter.objects.filter(birth__gte=datetime.today())
    # litters = models.Litter.objects.exclude(birth__gte=datetime.today()).order_by('-birth')
    # context = {
    #     'excepted_litters': excepted_litters,
    #     'litters': litters
    # }
    return HttpResponse(template.render({}, request))


def miot(request, id):
    template = loader.get_template("miot.html")
    litter = models.Litter.objects.get(pk=id)
    context = {
        'litter': litter
    }
    return HttpResponse(template.render(context, request))


def gallery(request):
    template = loader.get_template("gallery.html")
    photos = models.Gallery.objects.all()
    hashtags = models.HashTag.objects.all()

    context = {
        'photos': photos,
        'hashtags': hashtags,
    }
    return HttpResponse(template.render(context, request))


def felinoterapia(request):
    template = loader.get_template("felinoterapia.html")
    return HttpResponse(template.render(dict(), request))


def dyplomy(request):
    template = loader.get_template("dyplomy.html")
    return HttpResponse(template.render(dict(), request))


def pawpeds(request):
    template = loader.get_template("pawpeds.html")
    return HttpResponse(template.render(dict(), request))


def seminaria(request):
    template = loader.get_template("seminaria.html")
    return HttpResponse(template.render(dict(), request))


