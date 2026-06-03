from books.book import Book
from members.members import Member


class Library:
    def __init__(self):
        self._books = []
        self._members = []

    def add_book(self, book: Book):
        self._books.append(book)
        return "Book added successfully"

    def remove_book(self, book: Book):
        self._books.remove(book)
        return "Book removed successfully"
    
    def add_member(self, member: Member):
        self._members.append(member)

    def find_book_by_id(self, book_id):
        for book in self._books:
            if book._book_id == book_id:
                return book
        return None
    
    def display_all_books(self):
        result = "\n========== BOOK LIST ==========\n"
        for book in self._books:
            result += f"ID: {book.id} | Title: {book.title} | Author: {book.author} | "f"Type: {book.get_book_type()} | Available: {book.is_available()}\n"
        return result

    def search_by_title(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():   
                return f"Found: ID: {book.id} | Title: {book.title} | Author: {book.author} | Type: {book.get_book_type()} | Available: {book.is_available()}"
        return "Book not found."

    def search_by_author(self, author):
        results = []
        for book in self._books:
            if book.author.lower() == author.lower():   
                results.append(f"ID: {book.id} | Title: {book.title} | Type: {book.get_book_type()} | Available: {book.is_available()}")
        if results:
            return "Found book(s) by author:\n" + "\n".join(results)
        return "No books found by this author."