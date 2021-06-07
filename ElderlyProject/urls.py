"""ElderlyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from login.views import index, login,register,logout,info_show,info_edit,myfiles
from chat.views import chat
from overview.views import viewdoc, overview, viewpdf, publish, priavte
from upload.views import upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('info_show/',info_show),
    path('info_edit/',info_edit),
    path('captcha', include('captcha.urls')),
    path('chat/', chat),
    path('viewdoc/',viewdoc),
    path('viewpdf/',viewpdf),
    path('overview/<int:num>/',overview),
    path('upload/',upload),
    path('myfiles/',myfiles),
    path('publish/',publish),
    path('private/',priavte),
]

