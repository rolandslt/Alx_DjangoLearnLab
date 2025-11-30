from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework

from .models import Book
from .serializers import BookSerializer
"""
ListView:
- Returns all books.
- Read-only: available to anyone.
- Supports filtering, searching, and ordering.
- Filtering fields: title, author, publication_year
- Searching fields: title, author name
- Ordering fields: title, publication_year
"""
"""
Filtering:
    /api/books/?title=Book+Name
    /api/books/?author=1
    /api/books/?publication_year=2022

Searching:
    /api/books/?search=keyword
    Supports: title, author name

Ordering:
    /api/books/?ordering=title
    /api/books/?ordering=-publication_year
"""

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Filtering, searching, ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]


     # Filter options
    filterset_fields = ['title', 'author', 'publication_year']

    # Search options
    search_fields = ['title', 'author__name']

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
"""
DetailView:
- Return a single book by ID (pk).
- Read-only.
"""

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""
CreateView:
- Create a new book.
- Only authenticated users can create.
- Validates publication_year inside the serializer.
"""

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""
UpdateView:
- Update an existing book by ID.
- Only authenticated users can update.
"""

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""
DeleteView:
- Delete a book by ID.
- Only authenticated users can delete.
"""

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]