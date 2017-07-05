from django.conf.urls import url
from app_Book import views
#from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [url(r'^home/', views.book_home, name= 'index'),
	       url(r'^index/', views.index, name= 'index'),
               url(r'^books/(?P<c_name>[^/]+)/$', views.books, name = 'books'),
	       url(r'^book_det/(?P<b_id>[^/]+)/$', views.book_list, name = 'book_det'),
	       url(r'^wish_l/(?P<w_name>[^/]+)/$', views.wishlist, name = 'wish_list'),
	       url(r'^signup/$', views.signup, name = 'signup'),
	      url(r'^login/$', auth_views.login, name='login'),
              # url(r'^logout/$', views.logout, name='logout'),
	       
	       
	                   ]
