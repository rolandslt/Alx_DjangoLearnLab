from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permission(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
            return super().get_permissions()

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer