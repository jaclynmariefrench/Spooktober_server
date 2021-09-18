from spooktoberapi.views.search import EraSearchView, SpiritSearchView
from spooktoberapi.views.calendar_events import CalendarView
from spooktoberapi.views.user import UserView
from spooktoberapi.views.movie_tv import MovieTvView
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from spooktoberapi.views import login


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'movie_tv', MovieTvView, 'movie_tv')
router.register(r'era', EraSearchView, 'era')
router.register(r'spirit', SpiritSearchView, 'spirit')
router.register(r'users', UserView, 'user')
router.register(r'calendar', CalendarView, 'calendar')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login', login),
]
