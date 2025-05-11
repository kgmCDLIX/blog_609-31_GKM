from django.shortcuts import render
from articles.models import Article

def homepage(request):
    recent_articles = Article.objects.order_by('-date')[:3]  # последние 3 статьи
    return render(request, 'homepage.html', {
        'header': 'Homepage',
        'message': 'Welcome to my site!',
        'recent_articles': recent_articles
    })


def about(request):
    header = "About us"
    staff = ['John Cena', 'John Rogers', 'Timothy Smith']
    director = {"name": "Konstantin Maximovich", "img": '/director.png'}
    address = ('Lenina st. 1', 'New Surgut York', '648000', 'Russia')
    data = {"header": header, "staff": staff, "director": director,
            "address": address}
    return render(request, 'about.html', data)