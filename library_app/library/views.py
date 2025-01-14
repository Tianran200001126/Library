from django.shortcuts import render , get_object_or_404
from django.shortcuts import redirect
from .models import Book , Reader 


def list_books(request):
    books = Book.objects.all()
    readers = Reader.objects.all()
    return render(request,'library/list_book.html',{'books':books,'readers':readers})


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


def assign_book(request,book_pk):
    print(book_pk)
    book = get_object_or_404(Book,id=book_pk)
    if request.method == 'POST':
        reader_id = request.POST.get('reader')

        if not reader_id:
            return HttpResponse("Error: The reader is not selected, Please assign a book to a reader", status=400)

        try:
            reader = get_object_or_404(Reader,id=reader_id)
            book.loaned_to = reader
            book.save()
            return redirect('list_books')
        except Reader.DoesNotExist:
            return HttpResponse("Error: Reader not found in the database.", status=404)     


    return redirect('list_books')           



