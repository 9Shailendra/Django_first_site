from django.shortcuts import render, get_object_or_404
from .models import News
from django.contrib.syndication.views import Feed
from django.urls import reverse
import random


# Create your views here.

def news_list(request):
    recent_posts = News.objects.order_by('-created_at')[:5]
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news,'recent_posts': recent_posts})

def All_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/all_list.html', {'news': news})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    related_posts = News.objects.exclude(slug=slug).order_by('?')[:5]  # Simple example, customize as needed
    related_posts1 = News.objects.exclude(slug=slug).order_by('?')[:3]  # Fetch 3 random related posts
    return render(request, 'news/news_detail.html', {'news_item': news_item, 'related_posts': related_posts ,'related_posts1': related_posts1})

class LatestNewsFeed(Feed):
    title = "Latest News"
    link = "/rss/"
    description = "Updates on the latest news articles."

    def items(self):
        return News.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('news_detail', args=[item.slug])
    

    