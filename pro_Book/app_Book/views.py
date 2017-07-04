from django.http import HttpResponse
from django.shortcuts import render
from app_Book.models import Categories
def index(request):
    cat = Categories.objects.all()
    return render(request, 'app_Book/index.html',{'index': cat})
def book_list(request):
    #if Categories.cid = 'fiction'

    return render(request, 'app_Book/book_list.html',{})
