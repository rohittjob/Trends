from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<rank>[0-9]+)/$', views.detail, name='detail'),
    url(r'^tweet/$', views.tweet, name='tweet'),
]