from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'titleID': 'Beranda',
        'titleEN': 'Landing Page',
        'bg': 'bg-paper-white.jpg',
        'css': 'style.css',
        'navigasi': [
            ['/', 'Home'],
            ['/news', 'News'],
            ['/news/trending', 'Trending'],
            ['/news/latest', 'Latest'],
        ]
    }
    return render(request, 'index.html', context)

