from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('setup.urls')),  # Substitua 'seu_app' pelo nome do seu aplicativo
]
