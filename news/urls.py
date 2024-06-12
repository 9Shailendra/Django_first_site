from django.urls import path
from . import views
from .views import LatestNewsFeed

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('all/', views.All_list, name='all_list'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
    path('rss/', LatestNewsFeed(), name='rss_feed'),
    # path('category/<slug:slug>/', views.category_detail, name='category_detail'),
]
