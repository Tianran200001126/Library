from django.shortcuts import render , get_object_or_404
from .models import Book , Reader 


# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request,'library/list_book.html',{'books':books})


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, 'library/book_detail.html', {'book': book})    


def list_readers(request):  
    readers = Reader.objects.all()
    return render(request, 'library/list_reader.html', {'readers': readers})


def reader_detail(request, pk):
    reader = get_object_or_404(Reader, id=pk)
    borrowed_books = reader.borrowed_books.all()
    return render(request, 'library/reader_detail.html', {
        'reader': reader,
        'borrowed_books': borrowed_books,
    })