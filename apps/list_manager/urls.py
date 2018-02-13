from django.conf.urls import url
from .views import tmdb_search_view, marker_view, WatchListView, WatchListDeleteView


urlpatterns = [
    url('^search/', tmdb_search_view, name='search'),
    url('^mark/', marker_view, name='mark'),
    url('^manager', WatchListView.as_view(), name='manager_list'),
    url('^delete/(?P<slug>[^\.]+)/$', WatchListDeleteView.as_view(), name='manager_delete'),
]

