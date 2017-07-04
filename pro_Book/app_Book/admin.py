from django.contrib import admin
from app_Book.models import Categories, Book_List, Author,Book_Author,Book_details
admin.site.register(Categories)
admin.site.register(Book_List)
admin.site.register(Author)
admin.site.register(Book_Author)
admin.site.register(Book_details)

# Register your models here.
