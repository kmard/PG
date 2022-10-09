from django.shortcuts import render
from django.http import Http404
from .models import Book

# Create your views here.

def list_book(request):
    books = Book.objects.all()
    return render(request, 'book_store/list_books.html',{'books':books})

def book_detail(request,id):
    try:
        book = Book.objects.get(pk=id)
        return render(request, 'book_store/book_detail.html', {'book': book})
    except:
        raise Http404()
