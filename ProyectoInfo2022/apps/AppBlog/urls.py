from django.urls import path

from .views import frontpage, post_detail, banners

urlpatterns = [
    path('',frontpage, name='index'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('blog.html', banners,name='blog'),
]