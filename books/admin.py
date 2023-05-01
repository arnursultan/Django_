from django.contrib import admin
from books.models import Category, Book

admin.site.register(Book)
admin.site.register(Category)
