
from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.news_home, name='news_home'),
    url('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-det'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-upd'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-del')
]