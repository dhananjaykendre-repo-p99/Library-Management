from books.ebook import Ebook
from books.audio_book import AudioBook
from books.physical_book import PhysicalBook
from members.members import Member
from members.faculty import Faculty
from services.library import Library

def main():
    library = Library()
    
    library.add_book(Ebook(
        1,
        "Lord of the rings: The fellowship of the Ring",
        "John Tolkien",
        "ISBN101",
        15.5
    ))

    library.add_book(PhysicalBook(
        2,
        "Lord of the rings: The two towers",
        "John Tolkien",
        "ISBN102",
        "A1"
    ))

    library.add_book(AudioBook(
        3,
        "Lord of the rings: The return of the king",
        "John Tolkien",
        "ISBN103",
        500
    ))

    student = Member(1, "Dhananjay", 3)
    faculty = Faculty(2, "Yogesh Sharma")

    library.add_member(student)
    library.add_member(faculty)

    
    while True:
        print("\n========= LIBRARY MENU =========")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search Book By Title")
        print("5. Search Book By Author")
        print("6. View Borrowed Books")
        print("7. Exit")

        try:
            choice_str = input("Enter choice: ")
            if not choice_str.strip():
                continue
            choice = int(choice_str)
        except ValueError:
            print("Invalid choice.")
            continue

        if choice == 1:
            print(library.display_all_books())
        elif choice == 2:
            print(library.display_all_books())
            try:
                borrow_id_str = input("Enter Book ID to borrow: ")
                borrow_id = int(borrow_id_str)
            except ValueError:
                print("Invalid Book ID.")
                continue

            book_to_borrow = library.find_book_by_id(borrow_id)
            if book_to_borrow is not None:
                print(student.borrow_book(book_to_borrow))
            else:
                print("Book not found.")
        elif choice == 3:
            try:
                return_id_str = input("Enter Book ID to return: ")
                return_id = int(return_id_str)
            except ValueError:
                print("Invalid Book ID.")
                continue

            return_book = library.find_book_by_id(return_id)
            if return_book is not None:
                student.return_book(return_book)
            else:
                print("Book not found.")
        elif choice == 4:
            title = input("Enter title: ")
            print(library.search_by_title(title))
        elif choice == 5:
            author = input("Enter author: ")
            print(library.search_by_author(author))
        elif choice == 6:
            borrowed_books = student.get_borrowed_books()
            if not borrowed_books:
                print("No books borrowed.")
                continue

            print("\nBorrowed Books:")
            for book in borrowed_books:
                print(book.title)
        elif choice == 7:
            print("Exiting application...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()