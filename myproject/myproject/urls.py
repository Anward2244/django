"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from basic.views import movieInsert, getMoviesByGenrename, home, about, contact, services, htres, jsres, getreq, cityfil, pages, dataInsert

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('htres/', htres),
    path('jsres/',jsres),
    path('getreq/',getreq),
    path('city/',cityfil),
    path('pages/', pages),
    path('dataInsert/',dataInsert),
    path('movieInsert/', movieInsert),
    path('movieByGenre/<str:genre>', getMoviesByGenrename)
]
