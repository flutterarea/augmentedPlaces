from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('app/', views.demo, name = "app"),
    path('locations/', views.join, name = "locations"),
    path('accounts/profile/', views.profile, name = "profile"),
    path('', include('pwa.urls'))
]