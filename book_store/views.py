from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.

def list_book(request):
    books = Book.objects.all().order_by('-rating')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))

    return render(request, 'book_store/list_books.html',{'books':books,
                                                         'num_books':num_books,
                                                         'avg_rating':avg_rating,})

def book_detail(request,id):
    try:
        book = Book.objects.get(pk=id)
        return render(request, 'book_store/book_detail.html', {'book': book})
    except:
        raise Http404()

def book_detail_slug(request,slug):
    try:
        book = Book.objects.get(slug=slug)
        return render(request, 'book_store/book_detail.html', {'book': book})
    except:
        raise Http404()