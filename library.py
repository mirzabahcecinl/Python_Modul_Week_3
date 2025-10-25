import json
import os

# Book Classes
class Book:
    def __init__(self, title, author, publication_year,):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False
        self.borrowed_by = None
        

    def show_info(self):
        status = f"Borrowed by: {self.borrowed_by}" if self.is_borrowed else "Available"
        print(f"{self.title} by {self.author} ({self.publication_year}) - {status}")


    def borrow(self, user):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user.name
            user.borrowed_books.append(self.title)
            print(f"{user.name} borrowed {self.title}.")
        else:
            print("Book is already borrowed.")


    def return_book(self, user):
        if self.is_borrowed and self.borrowed_by == user.name:
            self.is_borrowed = False
            self.borrowed_by = None
            user.borrowed_books.remove(self.title)
            print(f"{user.name} returned {self.title}.")
        else:
            print("You cannot return this book.")
        

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
        }


    

class Novel(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def to_dict(self):
        data = super().to_dict()
        data["genre"] = self.genre
        return data
    

class Magazine(Book):
    def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue

    def to_dict(self):
        data = super().to_dict()
        data["issue"] = self.issue
        return data
    

# -------------------------------------
# User Class
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.borrowed_books = []

    def borrow_book(self, book):
        book.borrow(self)

    def return_book(self, book):
        book.return_book(self)

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("No borrowed books.")
        else:
            print("Borrowed Books:")
            for title in self.borrowed_books:
                print(f"- {title}")

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": self.borrowed_books
        }
    


# ---------------------------------------------------
# Library Class

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def show_all_books(self):
        print("\n All Books in Library:")
        for book in self.books:
            book.show_info()

    def login(self, name, password):
        user = self.find_user(name)
        if user and user.password == password:
            print(f"Welcome, {name}")
            return user
        print("Invalid username or password.")
        return None
    
    def save(self, filename):
        data = {
            "name": self.name,
            "books": [b.to_dict() for b in self.books],
            "users": [u.to_dict() for u in self.users]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def load(self, filename):
        if not os.path.exists(filename):
            print("No saved data found, opening new file.")
            return
        with open(filename, "r") as f:
            data = json.load(f)
        self.name = data["name"]
        self.books = []
        self.users = []

        for b in data["books"]:
            if b["type"] == "Novel":
                book = Novel(b["title"], b["author"], b["publication_year"], b.get("genre", "Unknown"))
            elif b["type"] == "Magazine":
                book = Magazine(b["title"], b["author"], b["publication_year"], b.get("issue", "N/A"))
            else:
                book = Book(b["title"], b["author"], b["publication_year"])
            book.is_borrowed = b["is_borrowed"]
            book.borrowed_by = b["borrowed_by"]
            self.books.append(book)


        for u in data["users"]:
            user = User(u["name"], u["password"])
            user.borrowed_books = u["borrowed_books"]
            self.users.append(user)

        print("Data loaded successfully.")



# -----------------------------------
# Main Program

def main():
    library = Library("Yellowstone Library")
    filename = "library_data.json"
    library.load(filename)

    print("\n Welcome to the Library Management System")
    current_user = None

    while not current_user:
        print("\n1 - Login")
        print("2 - Create Account")
        print("3 - Exit")
        choice = input("Select option: ")

        if choice == "1":
            name = input("Name: ")
            password = input("Password: ")
            current_user = library.login(name, password)

        elif choice == "2":
            name = input("Create username: ")
            password = input("Create password: ")
            if library.find_user(name):
                print("User already exists.")
            else:
                user = User(name, password)
                library.add_user(user)
                print("Account created successfully.")

        elif choice == "3":
            print("👋 Exiting program... Goodbye!")
            exit()
        else:
            print("Invalid option.")

    
    while True:
        print(f"\n Logged in as: {current_user.name}")
        print("1 - List all books")
        print("2 - Borrow a book")
        print("3 - Return a book")
        print("4 - Show my borrowed books")
        print("5 - Save and exit")

        option = input("Choose: ")

        if option == "1":
            library.show_all_books()
        elif option == "2":
            title = input("Enter book title to borrow: ")
            book = library.find_book(title)
            if book:
                current_user.borrow_book(book)
            else:
                print("Book not found.")
        elif option == "3":
            title = input("Enter book title to return: ")
            book = library.find_book(title)
            if book:
                current_user.return_book(book)
            else:
                print("Book not found.")
        elif option == "4":
            current_user.list_borrowed_books()
        elif option == "5":
            library.save(filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


