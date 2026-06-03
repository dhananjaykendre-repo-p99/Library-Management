from books.book import Book

class Ebook(Book):
    def __init__(self, book_id, title, author, isbn, file_size):
        super().__init__(book_id, title, author, isbn)
        self._file_size = file_size
    
    @property
    def file_size(self):
        return self._file_size
    
    def get_book_type(self):
        return "Ebook"