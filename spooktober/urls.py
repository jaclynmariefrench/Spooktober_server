from django.contrib import admin
from django.urls import path
from django.urls import path, include


v1_patterns = [
    path('auth/', include(('auth.urls', 'auth'))),
    path('users/', include(('users.urls', 'users'))),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include((v1_patterns, 'v1'))),
]