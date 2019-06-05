from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'vendor'
urlpatterns = [
    path('new', views.VendorCreate.as_view(), name='vendor_new'),
    # path('search', views.VendorList.as_view(), name='vendor_list'),
    path('view/<int:pk>', views.VendorView.as_view(), name='vendor_view'),
    path('edit/<int:pk>', views.VendorUpdate.as_view(), name='vendor_edit'),
    url(r'^delete/(?P<pk>\d+)/delete/$', views.vendor_delete, name='vendor_delete'),

    path('search/', views.vendor_search, name='vendor_search'),
]