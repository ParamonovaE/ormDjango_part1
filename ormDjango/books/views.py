from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from books.models import Book


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books,
    }
    return render(request, template, context)

def book_view(request, pub_date):
    try:
        book = Book.objects.get(pub_date=pub_date)
        books = list(Book.objects.all().order_by('pub_date'))
        current_index = books.index(book)
        if current_index > 0:
            previous_book = books[current_index - 1]
        else:
            previous_book = None

        if current_index < len(books) - 1:
            next_book = books[current_index + 1]
        else:
            next_book = None
        template_name = "books/book_detail.html"

        context = {
            'book': book,
            'previous_book': previous_book,
            'next_book': next_book,
        }


        return render(request, template_name, context)
    except Book.DoesNotExist:
        raise Http404("Книга не найдена")
