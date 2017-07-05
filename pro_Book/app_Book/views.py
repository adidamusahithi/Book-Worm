from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from app_Book.models import Categories, Book_List, Book_details
from django.contrib.auth.forms import UserCreationForm
from app_Book.forms import SignUpForm

#index is the html page and we r tranfering cat details to index templates
def book_home(request):
    #cat = Categories.objects.all()
    return render(request, 'app_Book/book_home.html',{})

def index(request):
    cat = Categories.objects.all()
    return render(request, 'app_Book/index.html',{'index': cat})
#books is the html page
#cname is the column in category table, c_name is the temp id
#cid is the id from category table and (cname = c_name).cid gives the comparision b/w name and if true gives cid from model

def books(request, c_name):
    fiction = Book_List.objects.filter(cid = Categories.objects.get(cname = c_name).cid)
    context = {'books': fiction}
    return render(request, 'app_Book/books.html', context)
#Bname is column from table and b_name is id

def book_list(request, b_id):
    #list(details) = Book_List.objects.filter(list(Bid) = Book_List.objects.get(Bname = b_name).Bid)
    bid = Book_List.objects.filter(Bid = b_id) 
    price = Book_details.objects.filter(Bid = b_id)
    context = {'Book_det': bid,'price': price}
    return render(request, 'app_Book/book_det.html', context)

def wishlist(request, w_name):
    wish = Book_List.objects.filter(Bid = w_name)
    context = {'wish_l': wish}
    return render(request, 'app_Book/wish_list.html', context)
    
    
def signup(request):
    print("enter signup")
    #HttpResponse(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            print("Logged in succesfully")
            return redirect("http://127.0.0.1:8000/app_Book/index/")
    else:
        form = SignUpForm()
    return render(request, 'app_Book/signup.html', {'form':form})


    

    

