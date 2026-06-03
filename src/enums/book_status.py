from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "avaiable"
    BORROWED = "borrowed"

    def __str__(self):
        return self.name