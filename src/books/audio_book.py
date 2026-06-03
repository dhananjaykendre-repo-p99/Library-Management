from books.book import Book

class AudioBook(Book):
    def __init__(self, book_id, title, author, isbn, duration):
        super().__init__(book_id, title, author, isbn)
        self._duration = duration

    @property
    def duration(self):
        return self._duration
    
    def get_book_type(self):
        return "Audiobook"