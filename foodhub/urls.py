"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from restaraunts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list, name="list"),
    path('detail/<int:restaraunt_id>/', views.restaraunt_detail, name="restaraunt_detail"),
    path('create/', views.create, name="restaraunt_create"),
    path('update/<int:restaraunt_id>/', views.update, name="restaraunt_update"),
    path('delete/<int:restaraunt_id>/', views.restaraunt_delete, name='restaraunt_delete'),

]
