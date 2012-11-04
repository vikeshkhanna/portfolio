from django.conf.urls.defaults import *
from home import views

urlpatterns = patterns('home.views',
    (r'^$','index'),
)
