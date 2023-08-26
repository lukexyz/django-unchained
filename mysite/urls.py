
from django.contrib import admin
from django.urls import path, include
from .views import hello_luke

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_luke, name='hello_luke'),
    path('accounts/', include('allauth.urls')),
]
