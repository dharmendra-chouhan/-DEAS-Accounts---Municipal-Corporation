from django.urls import path

from . import views

app_name = 'vendor'
urlpatterns = [
    path('new', views.VendorCreate.as_view(), name='vendor_new'),
    # path('search', views.VendorList.as_view(), name='vendor_list'),
    path('view/<int:pk>', views.VendorView.as_view(), name='vendor_view'),
    path('edit/<int:pk>', views.VendorUpdate.as_view(), name='vendor_edit'),
    path('delete/<int:pk>', views.VendorDelete.as_view(), name='vendor_delete'),
    path('search/', views.vendor_search, name='vendor_search'),
]