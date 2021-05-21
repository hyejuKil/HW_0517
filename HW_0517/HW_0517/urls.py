"""HW_0517 URL Configuration

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
import hwapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',hwapp.views.home, name='home'),
    path('hello/', hwapp.views.hello, name = 'hello'),
    path('<str:id>', hwapp.views.detail, name='detail'),
    path('new/', hwapp.views.new, name='new'),
    path('create/', hwapp.views.create, name='create'),
    path('edit/<str:id>', hwapp.views.edit, name = 'edit'),
    path('update/<str:id>', hwapp.views.update, name='update'),
    path('delete/<str:id>', hwapp.views.delete, name='delete'),
    path('',hwapp.views.sangsok, name='sangsok'),
]
