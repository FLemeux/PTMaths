"""
URL configuration for myfirstsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render, HttpResponse

from django.conf import settings
from django.conf.urls.static import static


from .views import *


urlpatterns=[
     path('admin/',admin.site.urls),
     path('home/',homepage_render),
     path('random/',randompage_render),
     path('cours_math/',cours_math_render, name='cours_math'),
     path('exo_math/',exo_math_render, name='exo_math'),
     path('DM_math/',DM_math_render, name='DM_math'),
     path('DS_math/',DS_math_render, name='DS_math'),
     path('info/',info_render, name='info'),
     path('TP/',TP_render, name='TP'),
     path('colles/',colles_render, name='colles'),
     ]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
