from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [

    path(r'receipt/', views.ReceiptList.as_view(), name='receipt-list'),
    path('receipt/add/$', views.ReceiptdetCreate.as_view(), name='receipt-add'),
    path('receipt/(?P<pk>[0-9]+)/$', views.ReceiptdetUpdate.as_view(), name='receipt-update'),
    path(r'receipt/(?P<pk>[0-9]+)/delete/$', views.ReceiptDelete.as_view(), name='receipt-delete'),

    # path('receipt/create/', views.ReceiptdetCreate.as_view(), name='receipt_create'),
    # path('receipt/create/', views.ReceiptList.as_view(), name='receipt-list'),
    # path('receipt/add/$', views.ReceiptdetCreate.as_view(), name='receipt-add'),
    # path('receipt/(?P<pk>[0-9]+)/$', views.ReceiptdetUpdate.as_view(), name='receipt-update'),
    # path('receipt/(?P<pk>[0-9]+)/delete/$', views.ReceiptDelete.as_view(), name='receipt-delete'),







    # path('receipt/add/$', views.receiptdetCreate.as_view(), name='receipt-add'),
    # path('receipt/(?P<pk>[0-9]+)/$', views.ReceiptList.as_view(), name='receipt-list'),
    # path('receipt/(?P<pk>[0-9]+)/delete/$', views.ReceiptList.as_view(), name='receipt-list'),


    # path('^$', views.receiptList.as_view(), name='receipt-list'),
    # url('^$', views.receiptList.as_view(), name='receipt-list'),
    # url(r'receipt/add/$', views.receiptdetCreate.as_view(), name='receipt-add'),
    # url(r'receipt/(?P<pk>[0-9]+)/$', views.receiptdetUpdate.as_view(), name='receipt-update'),
    # url(r'receipt/(?P<pk>[0-9]+)/delete/$', views.receiptDelete.as_view(), name='receipt-delete'),
]

