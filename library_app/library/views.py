from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from functools import wraps
from .models import Book, Reader
import uuid


def admin_required(view_func):
    """
    A decorator to ensure only admin users can access the view.
    Redirects non-admin users to the login page.
    """
    @wraps(view_func)
    def admin_check(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_staff:
            return HttpResponse("Access Denied: Admins Only", status=403)
        return view_func(request, *args, **kwargs)

    return admin_check


@login_required
@admin_required
def list_books(request):
    """
    Display a list of all books and readers.
    """
    books = Book.objects.all()
    readers = Reader.objects.all()
    return render(request, 'library/list_book.html', {'books': books, 'readers': readers})


@login_required
@admin_required
def book_detail(request, pk: uuid.UUID):
    """
    Display details about a specific book.
    """
    book = get_object_or_404(Book, id=pk)
    return render(request, 'library/book_detail.html', {'book': book})


@login_required
@admin_required
def list_readers(request):
    """
    Display a list of all readers.
    """
    readers = Reader.objects.all()
    return render(request, 'library/list_reader.html', {'readers': readers})


@login_required
@admin_required
def reader_detail(request, pk: uuid.UUID):
    """
    Display details for a specific reader.
    """
    reader, borrowed_books = get_reader_and_books(pk)
    return render(request, 'library/reader_detail.html', {
        'reader': reader,
        'borrowed_books': borrowed_books,
    })


@login_required
@admin_required
def assign_book(request, book_pk: uuid.UUID):
    """
    Assign a book to a reader. The user selects a reader and assigns the book to them.
    """
    book = get_object_or_404(Book, id=book_pk)
    if request.method == 'POST':
        reader_id = request.POST.get('reader')

        if not reader_id:
            return HttpResponse(
                "Error: Please select a reader to assign the book.",
                status=400
            )

        reader = get_object_or_404(Reader, id=reader_id)
        book.loaned_to = reader
        book.save()

    return redirect('list_books')


@login_required
def user_detail(request, pk: uuid.UUID):
    """
    Display details about a user and the books they have borrowed.
    """
    reader, borrowed_books = get_reader_and_books(pk)
    return render(request, 'library/user_detail.html', {
        'reader': reader,
        'borrowed_books': borrowed_books
    })


def get_reader_and_books(reader_id: uuid.UUID):
    """
    Helper function to fetch a reader and the books they've borrowed.
    """
    reader = get_object_or_404(Reader, id=reader_id)
    borrowed_books = reader.borrowed_books.all()
    return reader, borrowed_books


def custom_login(request):
    """
    Custom login view to handle both admin and users.
    Admins are redirected to the book list, while users are taken to their user detail page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_staff:
                return redirect('list_books')
            else:
                pk = user.reader.id
                return redirect('user_detail', pk=pk)

        return render(request, 'library/login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'library/login.html', {'form': form})
