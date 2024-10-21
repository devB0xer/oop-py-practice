class Book:
    
    title = None
    author = None
    year = None
    
    __titles = []
    __authors = []
    
    def __new__(cls, title, author, year, *args, **kwargs):
        
        if (title in cls.__titles) and (author in cls.__authors):
            print('book is already exist!')
            return None
        
        cls.__titles.append(title)
        cls.__authors.append(author)
        
        return super().__new__(cls)
        
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year