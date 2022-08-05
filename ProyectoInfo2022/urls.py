"""ProyectoInfo2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView
from ProyectoInfo2022.apps.AppBlog.views import frontpage, post_detail

urlpatterns = [
    path('',frontpage, name='frontapage'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),
    #--------------------
    path(
        route='index.html',
        view=TemplateView.as_view(template_name='blog/index.html'),
        name='index'
    ),
    path(
        route='about.html',
        view=TemplateView.as_view(template_name='blog/about.html'),
        name='about'
    ),
    path(
        route='blog.html',
        view=TemplateView.as_view(template_name='blog/blog.html'),
        name='blog'
    ),
    path(
        route='post-details.html',
        view=TemplateView.as_view(template_name='blog/post-details.html'),
        name='post-details'
    ),
    path(
        route='contact.html',
        view=TemplateView.as_view(template_name='blog/contact.html'),
        name='contact'
    ),
]
