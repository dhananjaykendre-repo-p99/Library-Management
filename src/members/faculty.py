from members import Member

class Faculty(Member):
    def __init__(self, member_id, name, max_book_allowed):
        super().__init__(member_id, name, max_book_allowed)
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
        super().borrow_book(book)

    def return_book(self, book: Book):
        super().return_book(book)