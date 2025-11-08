from relationship_app.models import Author, Book, Library

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a specific library
library_name = "Central Library"
books_in_library = Book.objects.filter(library__name=library_name)
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print("-", book.title)

# 3. Retrieve the librarian for a specific library
library = Library.objects.get(name=library_name)
print(f"\nLibrarian for {library_name}: {library.librarian.name}")
