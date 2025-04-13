from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # --------------- DJANGO URL's ----------------
    path('dev/admin/', admin.site.urls),
    path('media/', views.static.serve),

    # --------------- OTHER URL's -----------------
    path('accounts/', include('allauth.urls')),

    # -------------- PROJECT URL's ----------------
    path('', include('apps.pages.urls')),
    path('pears/', include('apps.pears.urls')),
]


# --------------------------- URLS EXTENDED ----------------------------
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
