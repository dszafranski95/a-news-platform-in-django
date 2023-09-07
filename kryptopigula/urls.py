# urls.py
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('editorial/<slug:slug>/', views.editorial, name='editorial'),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Use ckeditor URLs
    path('tutorials/', views.tutorials, name='tutorials'),
    path('press-release/<slug:slug>/', views.press_release, name='press-release'),
    path('news/<slug:slug>/', views.news, name='news'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
