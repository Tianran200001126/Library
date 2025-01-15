from django.db import models
from django.contrib.auth.models import User
import uuid

class Reader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4) 
    name = models.CharField(max_length=100)  # name of the reader
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False) # user model for authentication

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)  # book title
    author = models.CharField(max_length=100)  # book author
    loaned_to = models.ForeignKey(
        Reader, on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books'
    )  # tracks which reader borrowed the book 