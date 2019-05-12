from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/create/$', views.book_create, name='book_create'),
    url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]



# urlpatterns = [
#     path('search', views.BookList.as_view(), name='book_list'),
#     path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
#     path('new', views.BookCreate.as_view(), name='book_new'),
#     path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
#     path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
# ]



