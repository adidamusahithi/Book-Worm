from django.contrib import admin
from app_Book.models import Categories, Book_List, Author,Book_Author, Book_Details, Wishlist,Delivery
admin.site.register(Categories)
admin.site.register(Book_List)
admin.site.register(Author)
admin.site.register(Book_Author)
admin.site.register(Book_Details)
admin.site.register(Wishlist)
admin.site.register(Delivery)
# Register your models here.
