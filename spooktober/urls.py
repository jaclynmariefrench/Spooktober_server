from spooktoberapi.views.movie_tv import MovieTvView
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'movie_tv', MovieTvView, 'movie_tv')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('allauth.urls')),
]
