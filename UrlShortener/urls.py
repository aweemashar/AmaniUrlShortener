from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'create_short_url/', views.create_short_url, name='shorten_url'),
    re_path(r'get_original_url/(?P<url>.+)$', views.get_original_url, name='original_url'),
]