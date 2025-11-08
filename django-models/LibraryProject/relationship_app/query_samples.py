from relationship_app.models import Author, Library

# 1. Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()  # use .all() on related_name
print(f"Books by {author.name}:")
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a specific library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()  # use .all() on ManyToManyField
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print("-", book.title)

# 3. Retrieve the librarian for a library
print(f"\nLibrarian for {library.name}: {library.librarian.name}")
