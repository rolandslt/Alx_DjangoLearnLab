from django.contrib import admin
from django.urls import path
from .views import list_books , LibraryDetailView , register
from . import views
from  django.contrib.auth.views import LoginView , LogoutView
from .admin_view.views import admin_view
from .librarian_view.views import librarian_view
from .member_view.views import member_view



urlpatterns = [
  
    path('relationship_app/', list_books, name='list_books'),
    path('relationship_app/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('relationship_app/', views.register.as_view(), name='register'),
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
]
