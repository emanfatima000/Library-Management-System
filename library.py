class Book():
    def __init__(self, book_id,title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book is issued successfully")
        else:
            print("Book is not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfuly")
        else:
            print("Book was already in library")

    def display(self):
        print("=====BOOK DETAILS=======")
        print("Book_ID: ",self.book_id)
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Category: ",self.category)
        print("Available: ",self.available)

    def is_available(self):
        print("Available: ",self.available)

class Library():

    def __init__(self):
        self.books = []

    def save_to_file(self):
        file = open("books.txt","w")
        for book in self.books:
            data = f"{book.book_id},{book.title},{book.author},{book.category},{book.available}\n"
            file.write(data)

        file.close()
        print("Data saved to file")

    def load_from_file(self):
        self.books = []

        try:
            file = open("books.txt","r")

            for line in file:
                data = line.strip().split(",")

                book_id = int(data[0])
                title =(data[1])
                author =(data[2])
                category =(data[3])
                available =(data[4])=="True"

                book = Book(book_id,title,author,category)
                book.available = available

                self.books.append(book)

            file.close()
            print("Data loaded from file")

        except FileNotFoundError:
            print("No saved data found")

    def add_book(self,new_book):
        for book in self.books:
            if book.book_id == new_book.book_id:
                print("Book ID already exists!")
                return
        self.books.append(new_book)
        print("Book added successfuly")

    def view_all(self):
        if not self.books:
            print("No book available")
            return
        for book in self.books:
            book.display()

    def search_book(self,book_name):
        for book in self.books:
            if book.title.lower() == book_name.lower():
                book.display()
                return
        print("Not found")

    def remove_book(self,book_id):
        for book in self.books[:]:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found")

    def issue_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.borrow_book()
                return
        print("Book not found")

    def return_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                return
        print("Book not found")

    def view_available_books(self):
        if not self.books:
            print("No book available")
            return
        for book in self.books:
            if book.available:
                book.display()

    def search_by_id(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.display()
                return
        print("Book not found")

    def id_exists(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                return True
        return False
        
library = Library()
library.load_from_file()
while True:
    print("====LIBRARY MENU====")
    print("1.Add Book ")
    print("2.View Books")
    print("3.Save & Exit")
    print("4.Search Book")
    print("5.Delete Book")
    print("6.Issue Book")
    print("7.Return Book")
    print("8.View Available Books")
    print("9.Search by Id:")

    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        if library.id_exists(book_id):
            print("Book_ID already exists!")
            continue

        title = input("Enter Title: ")
        author = input("Enter author: ")
        category = input("Enter Category: ")
        new_book = Book(book_id,title,author, category)
        library.add_book(new_book)

    elif choice == 2:
        library.view_all()

    elif choice == 3:
        library.save_to_file()
        break

    elif choice == 4:
        book_name = input("Enter a title to search book: ")
        library.search_book(book_name)

    elif choice == 5:
        book_id = int(input("Enter Book_ID to delete: "))
        library.remove_book(book_id)

    elif choice == 6:
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == 7:
        book_id = int(input("Enter book ID to return: "))
        library.return_book(book_id)

    elif choice == 8:
        library.view_available_books()

    elif choice == 9:
        book_id = int(input("Enter book_id: "))
        library.search_by_id(book_id)
        
    else:
        print("Invalid choice")

