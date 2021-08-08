from django.shortcuts import render
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, template, context)

def books_date_view(request, slug):
    template = 'books/books_date.html'
    books = Book.objects.filter(pub_date=slug)
    next_book = Book.objects.all().order_by('pub_date').filter(pub_date__gt=slug)[:1]
    if len(next_book) != 0:
        next_date = next_book[0].pub_date
    else:
        next_date = False
    previous_book = Book.objects.all().order_by('-pub_date').filter(pub_date__lt=slug)[:1]
    if len(previous_book) != 0:
        previous_date = previous_book[0].pub_date
    else:
        previous_date = False
    context = {
        'books' : books,
        'next_date' : str(next_date),
        'previous_date' : str(previous_date)
    }
    return render(request, template, context)
