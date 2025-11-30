from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer
"""
ListView:
- Returns all books.
- Read-only: available to anyone.
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
     filter_backends = [SearchFilter]
    search_fields = ['title', 'author__name']

"""
DetailView:
- Return a single book by ID (pk).
- Read-only.
"""

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

"""
CreateView:
- Create a new book.
- Only authenticated users can create.
- Validates publication_year inside the serializer.
"""

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

"""
UpdateView:
- Update an existing book by ID.
- Only authenticated users can update.
"""

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

"""
DeleteView:
- Delete a book by ID.
- Only authenticated users can delete.
"""

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]