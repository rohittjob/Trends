from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/(?P<type>[hm]+)/(?P<rank>[0-9]+)/$', views.detail, name='detail'),
    url(r'^tweet/$', views.tweet, name='tweet'),
]