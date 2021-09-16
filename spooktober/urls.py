from spooktoberapi.views.user import UserView
from spooktoberapi.views.movie_tv import MovieTvView
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from spooktoberapi.views import login


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'movie_tv', MovieTvView, 'movie_tv')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login', login),
]
