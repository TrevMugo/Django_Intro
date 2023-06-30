from django.shortcuts import render


def nyumbani(request):
    return render(request, 'index.html')


def kuhusu(request):
    return render(request, 'about.html')


def mapicha(request):
    return render(request, 'gallery.html')
