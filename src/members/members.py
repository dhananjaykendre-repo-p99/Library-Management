from books.book import Book

class Member:
    def __init__(self, member_id, name, max_books_allowed):
        self._member_id = member_id
        self._name = name
        self._max_books_allowed = max_books_allowed
        self._borrowed_books = []

    @property
    def member_id(self):
        return self._member_id
    
    @property
    def name(self):
        return self._name

    @property
    def max_books_allowed(self):
        return self.max_books_allowed

    def get_borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book: Book):
        if len(self._borrowed_books) >= self.max_books_allowed:
            return "Borrow limit is reached"
        
        if not book.is_available():
            return "Book is borrowed"
        
        book.borrow_book()
        self._borrowed_books.append(book)
        return "Book borrowed successfully"

    def return_book(self, book: Book):
        if not book in self._borrowed_books:
            return "Book is not borrowed"
        
        self._borrowed_books.remove(book)
        book.return_book()
        return "Book returned successfully"