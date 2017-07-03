from django.http import HttpResponse
from django.shortcuts import render
from app_Book.models import Categories
def index(request):
    cat = Categories.objects.all()
    return render(request, 'app_Book/index.html',{'index': cat})
def second(request):
    return render(request, 'app_Book/second.html',{})
