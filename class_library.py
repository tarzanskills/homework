class Library:
    def __init__(self,type,location,year,librarian,num_books):
        self.type = type
        self.location = location
        self.establish_year = year
        self.librarian = librarian
        self.num_books = num_books
    def get_address(self):
        print("Address of library is printed", self.location)

waterloo = Library(False, "England", 1969, "Emma Watson", 88900)
print("The librarian is", waterloo.librarian)
waterloo.get_address()