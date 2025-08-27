
class Library:

    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks(self): # It finds all books in the library 

        print(f"We have following books in our library: {self.name}")

        for book in self.booklist:
            print(book)

    def addBooks(self, book): # It adds new books
        if book in self.booklist:
            print('Book already exists')
        else:
            self.booklist.append(book)
            print('Book added')

    def lendBook(self, book, user):  # It keeps records of all the borrowed books
        if book in self.booklist:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print('Book has been lended. Database updated')
            else:
                print(f'Book is already being used by {self.lendDict[book]}')
        else:
            print('Apologies! we don\'t have this book in our library')

    def returnBook(self, book): #It updates based on the returned books
        if book in self.lendBook.keys():
            self.lendDict.pop(book)
            print('book Returned Successfully')
        else:
            print('The book doesn\'t exist in the Book Lending Datbase')
    
def main():
    while True():
        print(f'Welcome to the {Library.name}')
        choice = "[1] - Display Books\n" \
        "[2] - Lend a Book\n" \
        "[3] - Add a Book"
        "[4] - Return a Book"
        print(choice)