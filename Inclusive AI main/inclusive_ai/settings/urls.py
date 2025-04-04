from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dev/admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('main.urls')),
]
