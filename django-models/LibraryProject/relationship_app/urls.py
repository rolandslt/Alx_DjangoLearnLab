from django.contrib import admin
from django.urls import path
from .views import list_books, library_detail
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', views.list_books, name='list_books'),
    path('relationship_app/', views.library_detail.as_view(), name='library_detail'),
]
