from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurs/',include('courses.urls')),
    path('account/',include('account.urls')),
    path('',include('pages.urls')),
]   + static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)