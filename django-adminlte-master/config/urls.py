from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.pages.urls')),        # ONLY ONE root
    path('datatable/', include('apps.dyn_dt.urls')),
    path('api/', include('apps.dyn_api.urls')),
    path('charts/', include('apps.charts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
