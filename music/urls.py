from django.conf.urls.defaults import *

urlpatterns = patterns('music.views',
    (r'^status/?$','status'),
)
