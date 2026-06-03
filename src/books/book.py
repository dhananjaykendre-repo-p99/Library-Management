from abc import abstractmethod
from interfaces.borrowable import Borrowable
from enums.book_status import BookStatus

class book(Borrowable):
    def __init__(self, book_id, title, author, isbn):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._isbn = isbn
        self._status = BookStatus.AVAILABLE

    @property
    def id(self):
        return seld._book_id
    
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    
    @property
    def isbn(self):
        return self._isbn

    def is_available(self):
        return self._status == BookStatus.AVAILABLE
    
    def borrow_book(self):
        self._status = BookStatus.BORROWED
    
    def return_book(self):
        self._status = BookStatus.AVAILABLE

    @abstractmethod
    def get_book_type(self):
        pass