from django.db import models
import uuid

class Reader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)  # Unique identifier
    email = models.EmailField(unique=True)  # Email of the reader
    name = models.CharField(max_length=100)  # Name of the reader



class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique identifier
    title = models.CharField(max_length=200)  # Book title
    author = models.CharField(max_length=100)  # Book author
    loaned_to = models.ForeignKey(
        Reader, on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books'
    )  # Tracks which reader borrowed the book 
