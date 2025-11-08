from django.contrib import admin
from django.urls import path
from .views import list_books , LibraryDetailView , SignUpView
from . import views
from  django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', list_books, name='list_books'),
    path('relationship_app/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'relationship_app/logout.html'), name='logout'),
    path('relationship_app/', SignUpView.as_view(template_name = 'relationship_app/register.html'), name='register')
]
