from django.conf.urls import url
from .views import manager_view, check_view


urlpatterns = [
    url('^manager/', manager_view, name='manager'),
    url('^check/', check_view, name='check'),
]

