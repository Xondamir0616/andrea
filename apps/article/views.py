from django.shortcuts import render
from .models import Article, Category, Comment, Tag

def index(request):
    articles = Article.objects.all().order_by('-id')
    context = {
        'articles_list': articles
    }
    
    
    return render(request, 'index.html',context)


def single(request):
    articles = Article.objects.all().order_by('-id')
    slug = Article.slug
    context = {
        'articles_list': articles
    }
    
    
    return render(request, 'single.html',context)

def travel(request):
    articles = Article.objects.all().order_by('-id')
    context = {
        'articles_list': articles
    }
    
    
    return render(request, 'travel.html',context)

def fashion(request):
    articles = Article.objects.all().order_by('-id')
    context = {
        'articles_list': articles
    }
    
    
    return render(request, 'fashion.html',context)

