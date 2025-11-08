from django.shortcuts import render

# Create your views here.
from .models import Book, Author, Librarian ,Library
from django.views.generic import ListView

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class library_detail(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('books_author')