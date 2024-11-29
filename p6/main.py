from Book import Book
from Car import Car

book = Book('some_title', 'some_author', 10)
book.set_author('another_author').set_pages(100)
print(book.display_info())

беэмве = Car('bmw')
беэмве.set_mileage(300000).set_year(1990)
print(f"{беэмве.model} {беэмве.get_year()} {беэмве.get_mileage()}")