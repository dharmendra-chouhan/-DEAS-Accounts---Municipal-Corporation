from django.conf.urls import url
from django.contrib import admin
from subledger import views

from . import views

app_name = 'subledger'
urlpatterns = [
    url(r'^$', views.subledger_search, name='subledger_search'),
    url(r'^new$', views.SubledgerCreate, name='subledger_new'),
    url(r'^edit/(?P<pk>\d+)$', views.SubledgerUpdate, name='subledger_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.SubledgerDelete, name='subledger_delete'),
    url(r'^delete/(?P<pk>\d+)$', views.subledger, name='subledger'),
    
    # url(r'^delete/(?P<pk>\d+)$', views.Subledger_master_delete, name='book_delete'),
    # url(r'^books/(?P<pk>\d+)/delete/$', views.Subledger_master_delete, name='book_delete'),
]