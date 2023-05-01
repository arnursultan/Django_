from django.shortcuts import render, get_object_or_404

from books.models import Book, Category


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        "books": books,
        "categories": categories,
    }
    return render(request, "books/index.html", context)


def category_detail(request, name):
    category = get_object_or_404(Category, name=name)
    books = Book.objects.filter(category__name=name)

    return render(request, "books/category_detail.html", {"category": category, "books": books})