from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.record_table),
    url(r'^form/new/$', views.record_form, name='record_form'),
    url(r'^form/(?P<pk>[0-9]+)/edit/$', views.record_edit, name='record_edit'),
]