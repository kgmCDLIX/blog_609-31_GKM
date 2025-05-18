from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArticleForm
from articles import forms
from articles.models import Article


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_item.html', {'article': article} )

@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = forms.ArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})