from django.conf.urls import  url
from kd_list import views

urlpatterns = [
   url(r'^$', views.list_all, name = "list_all"),
   url(r'^kd/(?P<pk>\d+)/$', views.kd, name = "kd"),
   url(r'^kd/new/$', views.kd_new, name='kd_new'),
   url(r'^register/$', views.register, name='register'),
   url(r'^profile/$', views.profile, name='profile'),
]
