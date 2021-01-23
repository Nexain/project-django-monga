from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titleID': 'Berita',
        'titleEN': 'News',
        'css': 'style.css',
        'css2': 'style2.css',
        'navigasi': [
            ['/', 'Home', ''],
            ['/news', 'News', 'active'],
            ['/news/trending', 'Trending', ''],
            ['/news/latest', 'Latest', ''],
        ]
    }
    return render(request, 'index.html', context)

def trending(request):
    context = {
        'titleID': 'Berita Populer',
        'titleEN': 'Trending News',
        'css': 'style.css',
        'image': 'nature-1.jpg',
        'navigasi': [
            ['/', 'Home', ''],
            ['/news', 'News', ''],
            ['/news/trending', 'Trending', 'active'],
            ['/news/latest', 'Latest', ''],
        ]
    }
    return render(request, 'index.html', context)

def latest(request):
    context = {
        'titleID': 'Berita Terbaru',
        'titleEN': 'Hot News',
        'css': 'style.css',
        'navigasi': [
            ['/', 'Home', ''],
            ['/news', 'News', ''],
            ['/news/trending', 'Trending', ''],
            ['/news/latest', 'Latest', 'active'],
        ]
    }
    return render(request, 'index.html', context)