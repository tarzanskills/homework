
class Library:
    def __init__(self,type,location,year,librarian,num_books):
        self.type = type
        self.location = location
        self.established_year = year
        self.librarian = librarian
        self.num_books = num_books
    def get_address(self):
        print("Address of library is printed", self.location)

library = Library("all_types", "India", 2010, "Alex Thomas", 5000)
print("The librarian is", library.librarian)
print("The libray was established at",library.established_year)
library.get_address()
