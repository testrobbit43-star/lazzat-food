"""
Main URL Configuration for Lazzat Food Backend.
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # API Documentation (Swagger & ReDoc)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # API Routes
    path('api/v1/', include('apps.restaurant.urls', namespace='restaurant')),
    path('api/auth/', include('apps.core.urls', namespace='auth')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = 'Lazzat Food Administration'
admin.site.site_title = 'Lazzat Food Admin'
admin.site.index_title = 'Xush kelibsiz Lazzat Food Admin Paneliga'
