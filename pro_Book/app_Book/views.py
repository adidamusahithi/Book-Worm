from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'app_Book/index.html',{})
def second(request):
    return render(request, 'app_Book/second.html',{})
