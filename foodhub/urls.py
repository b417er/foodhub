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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('list/', views.list, name="list"),
    path('detail/<int:restaraunt_id>/', views.restaraunt_detail, name="restaraunt_detail"),
    path('create/', views.create, name="restaraunt_create"),
    path('create_item/<int:restaraunt_id>/', views.create_item, name="create_item"),
    path('update/<int:restaraunt_id>/', views.update, name="restaraunt_update"),
    path('delete/<int:restaraunt_id>/', views.restaraunt_delete, name='restaraunt_delete'),
    path('favourite_restaraunt/<int:restaraunt_id>/', views.favourite_restaraunt, name='favourite_restaraunt'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
