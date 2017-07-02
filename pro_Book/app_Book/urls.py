from django.conf.urls import url
from app_Book import views
urlpatterns = [url(r'^index/', views.index, name= 'index'),
               url(r'^[A-Za-z]second/',views.second,name = 'second'),
    ]
