class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def display_books(self):
        status = 'available' if self.available else 'Issued'
        print('Book Id: ', self.book_id)
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('Category: ', self.category)
        print('status: ', status)

    def issue_book(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def display_members(self):
        print('Member ID: ', self.member_id)
        print('Member name: ', self.name)
        print('Member email: ', self.email)
        print('Borrowed Books')
        if len(self.borrowed_books) == 0:
            print('No Books Borrowed')
        else:
            for book in self.borrowed_books:
                print(self.title)

    def borrow_book(self, book):
        self.borrowed_books = self.borrowed_books
