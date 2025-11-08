from django.shortcuts import render

# Create your views here.
from .models import Book
from .models import Library

from django.contrib.auth.forms import UserCreationForm
from django.urls import resolvers_lazy
from django.views.generic import CreateView
from django.contrib.auth import login , logout
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('books_author')
    
class register(CreateView):
    form_class = UserCreationForm()
    success_url = resolvers_lazy('login')
    template_name = 'relationship_app/register.html'


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')