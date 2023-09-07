# views.py
from django.shortcuts import render, get_object_or_404
from .models import Editorial, CryptoAnalysis, PressRelease, News

def index(request):
    editorials = Editorial.objects.all()[:45]
    crypto_analyses = CryptoAnalysis.objects.all()
    press_releases = PressRelease.objects.all()[:4]
    news = News.objects.all().order_by('-pub_date')[:23]
    context = {
        'editorials': editorials,
        'crypto_analyses': crypto_analyses,
        'press_releases': press_releases,
        'news': news,  # Add this line
    }
    return render(request, 'index.html', context)



def editorial(request, slug):
    editorial = get_object_or_404(Editorial, slug=slug)
    return render(request, 'editorial.html', {'editorial': editorial})

def tutorials(request):
    tutorials = Editorial.objects.all()
    return render(request, 'tutorials.html', {'tutorials': tutorials})

# views.py
def press_release(request, slug):
    press_release = get_object_or_404(PressRelease, slug=slug)
    return render(request, 'press_release.html', {'press_release': press_release})

def news(request, slug):
    news = get_object_or_404(News, slug=slug)
    news.views += 1  # Increase the views by 1
    news.save()  # Don't forget to save the object
    return render(request, 'news.html', {'news': news})
