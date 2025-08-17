"""
URL configuration for marvelweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('movies-sequence/',views.printallmarvelmoviesinsequence,name='move sequence'),
    path('home/',views.home,name='home'),
    path('create-superhero/',views.createsuperhero,name='create superhero'),
    path('addsuperhero/',views.addsuperhero,name='Added'),
    path('search-superhero/',views.searchsuperhero,name='search superhero'),
    path("displaysuperhero/",views.displaysuperhero,name='display superhero'),
    path('fan-stories/',views.fanstory,name='fan story'),
    path('add-fan-story/',views.addfanstory,name='add fan story'),
    path('submit-fan-story/',views.submitfanstory,name='submit fan story'),
    path('showfanstory/',views.showfanstory,name='fan story'),
    path('downloadmovie/',views.serchmoviename,name='searchmoviename'),
    path('downlodmovietourl/',views.downlodmovietourl,name='downlodmovietourl'),
    path('upcomeingmarvelmovies/',views.upcomeingmarvelmovies,name='upcomeingmarvelmovies')

]