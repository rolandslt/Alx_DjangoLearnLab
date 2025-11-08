from .models import Author, Book, Library, Librarian

books_by_author = Book.objects.filter(author_name="J.K. Rowling")
print("Books by J.K. Rowling:")
for book in books_by_author:
    print("-", book.title)

books_in_library = Book.objects.filter(library_name="Central Library")
print("n\Books in central Library:")
for book in books_in_library:
    print("-", book.title)

library = Library.objects.get(name="Central Library")
print("\nLibrary for Central Library: ", library.librarian.name)
