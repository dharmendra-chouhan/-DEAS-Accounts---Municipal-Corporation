from django.urls import path

from .import views

app_name = 'bankmaster'
urlpatterns = [
    path('new', views.BankmasterCreate.as_view(), name='bankmaster_new'),
    path('search', views.BankmasterList.as_view(), name='vendor_list'),
    path('view/<int:pk>', views.BankmasterView.as_view(), name='bankmaster_view'),
    path('edit/<int:pk>', views.BankmasterUpdate.as_view(), name='bankmaster_edit'),
    path('delete/<int:pk>', views.BankmasterDelete.as_view(), name='bankmaster_delete'),
    path('search/', views.bankmaster_search, name='bankmaster_search'),
]