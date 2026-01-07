class Book:
    def __init__(self, name, authors, publisher, isbn, year):
        self.name = name
        self.authors = authors     
        self.n = len(authors)      
        self.publisher = publisher
        self.isbn = isbn
        self.year = year
    def display(self):
         def print_data(self):
        print("\n\n")
        print(f"Name: {self.name}")
        print(f"Number of authors: {self.n}")
        print(f"Authors: {self.authors}")
        print(f"Publisher: {self.publisher}")
        print(f"ISBN: {self.ISBN}")
        print(f"Year: {self.year}")

class CourseBook(Book):
    def __init__(self, name, authors, publisher, isbn, year, course):
        super().__init__(name, authors, publisher, isbn, year)
        self.course = course
    # Method Overriding (Extending)
    def display(self):
        super().display() 
        print(f"Course: {self.course}") 
auth_list = ["H.M. Deitel", "P.J. Deitel"]
my_book = CourseBook("Python Programming", auth_list, "Pearson", "978-0134034287", 2024, "Computer Science")

my_book.display()
