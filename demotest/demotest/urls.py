from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),  # 🔥 This enables routes from your calc app
]
