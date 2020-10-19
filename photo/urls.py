"""myFirstDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'app_name_photo'  # 为 {% url %} 服务，为了测试，故意加了app_name，正常来说直接和模块名称一样就可以

urlpatterns = [
#    url(r'^upload/$',photo.upload,name="upload"),
#    url(r'^result/$',photo.result,name="result"),
    path('',views.index,name="index"),
    path('upload/',views.upload,name='path_upload'),     # name 也是为了 {% url %} 服务,同理前面加 path 也是为了测试
    path('result/',views.result,name='result'),
]
