class Book:
    def __init__(self):
        self.books = []
    def add_book(self, name, author, year):
        self.books.append({"название": name, "автор": author, "год": year})
    def display_info(self):
        for book in self.books:
            print(book)

t1 = Book()
t1.add_book("к1", "а1", 1860)
t1.add_book("к2", "а2", 1840)
t1.display_info()