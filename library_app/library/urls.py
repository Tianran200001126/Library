from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/<uuid:pk>/', views.book_detail, name='book_detail'),
    path('readers/', views.list_readers, name='list_readers'),
    path('readers/<uuid:pk>/', views.reader_detail, name='reader_detail'),
    path('books/<uuid:book_pk>/assign/', views.assign_book, name='assign_book'),
    path('login/', views.custom_login, name='login'),
    path('user/<uuid:pk>/', views.user_detail, name='user_detail')
]
