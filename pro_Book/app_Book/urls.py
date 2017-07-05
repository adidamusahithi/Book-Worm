from django.conf.urls import url
from app_Book import views
urlpatterns = [url(r'^index/', views.index, name= 'index'),
               url(r'^books/(?P<c_name>[^/]+)/$', views.books, name = 'books'),
	       url(r'^book_det/(?P<b_id>[^/]+)/$', views.book_list, name = 'book_det'),
	       url(r'^wish_l/(?P<w_name>[^/]+)/$', views.wishlist, name = 'wish_list'),
               
    ]
