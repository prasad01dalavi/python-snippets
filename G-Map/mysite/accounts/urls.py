from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name':'accounts/logout.html'}),
    url(r'^login/dashboard/$', views.dash, name = 'dash'),
    url(r'^login/dashboard/gmap/$', views.gmap, name = 'gmap')
    ]
