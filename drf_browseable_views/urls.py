"""drf_browseable_views URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MockView, mock_view, MockViewSet

# in this demo, we don't register /admin/ in the router to show how you can
# exclude a route from appearing in the browseable API. the browseable API will
# only show views that are registered in the router.

django_view_router = DefaultRouter()
# TODO: django-class2 and drf-viewset do not work
# `basename` is required:
django_view_router.register(
    'django-class1', MockView.as_view(), basename='example1.1')
django_view_router.register('django-class2', MockView, basename='example1.2')
django_view_router.register('django-function', mock_view, basename='example2')
django_view_router.register('drf-viewset', MockViewSet, basename='example3')
# the browseable API should be at / and should display the above four routes

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(django_view_router.urls)),
    path('', include((django_view_router.urls, 'drf'))),  # application namespace
]

urlpatterns += django_view_router.urls
