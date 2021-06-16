from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('arr_app.urls')),
    path('', include('usermanagement.urls')),
    path('users/', include('usermanagement.urls')),
    path('api/', include('rest_framework.urls')),
    
]


