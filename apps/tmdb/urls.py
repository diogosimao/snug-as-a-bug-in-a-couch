from django.conf.urls import url
from .views import query_view


urlpatterns = [
    url('^query/', query_view, name='query'),
]