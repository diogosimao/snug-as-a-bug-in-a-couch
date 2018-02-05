from django.conf.urls import url
from .views import tmdb_search_view, marker_view


urlpatterns = [
    url('^search/', tmdb_search_view, name='search'),
    url('^mark/', marker_view, name='mark'),
]

