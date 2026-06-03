from books.book import Book

class PhysicalBook(Book):
    def __init__(self, book_id, title, author, isbn, shelf_location):
        super().__init__(book_id, title, author, isbn)
        self._shelf_location = shelf_location
    
    @property
    def shelf_location(self):
        return self._shelf_location

    def get_book_type(self):
        return "Physical Book"