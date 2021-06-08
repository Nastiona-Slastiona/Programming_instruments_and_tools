from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from mainboard import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('memacc/', include('memacc.urls')),
    path('',  views.post_list, name='post_list'),
    path('mainboard/', include('mainboard.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)