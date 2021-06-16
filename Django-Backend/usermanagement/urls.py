from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.UserViewSet, basename='UserLocationView')


urlpatterns = [
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dash/', views.dash, name = "dash"),
    path('users/dash/', views.dash, name = "dash"),
    path('locations/', include(router.urls)),
    path('update_location/', views.update_location, name='update_location'),
    
]