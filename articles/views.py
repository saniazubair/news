from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article_detail.html', {'article': article})

def category_filter(request, id):
    article = Article.objects.filter(category_id = id)
    return render(request, 'category.html', {'article': article})