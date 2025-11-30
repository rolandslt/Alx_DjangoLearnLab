from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


"""
BookSerializer:
- Serializes all fields of Book.
- Includes custom validation to prevent future publication years.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


"""
AuthorSerializer:
- Serializes the Author model.
- Includes nested BookSerializer to show all books written by the author.
- Uses the 'books' related_name defined in the Book model.
"""
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
