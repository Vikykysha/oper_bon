from django.conf.urls import  url
from kd_list import views

urlpatterns = [
   url(r'^$', views.list_all, name = "list_all"),
   url(r'^kd/(?P<pk>\d+)/$', views.kd, name = "kd"),
   url(r'^kd/new/$', views.kd_new, name='kd_new'),
   url(r'^register/$', views.register, name='register'),
   url(r'^profile/$', views.profile, name='profile'),
   url(r'^kd/(?P<pk>\d+)/remove/$', views.kd_remove, name='post_remove'),
   url(r'^kd/(?P<pk>\d+)/kd_edit/$', views.kd_edit, name='kd_edit'),
]
