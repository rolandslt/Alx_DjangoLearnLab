from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', views.list_books, name='list_books'),
    path('relationship_app/', views.LibraryDetailView.as_view(), name='library_detail'),
]
