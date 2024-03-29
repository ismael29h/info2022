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
from django.urls import path, include

from django.views.generic import TemplateView 

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Posts y comentarios
    path('', include(('ProyectoInfo2022.apps.AppBlog.urls', 'AppBlog'), namespace='posts')),
    # Usuarios
    path('', include(('ProyectoInfo2022.apps.AppUsers.urls', 'AppUsers'), namespace='usuarios')),
    # Acerca de...
    path(
        route='about.html',
        view=TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    # Contacto
    path(
        route='contact.html',
        view=TemplateView.as_view(template_name='contact.html'),
        name='contact'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

