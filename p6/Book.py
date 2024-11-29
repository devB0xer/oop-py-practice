class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self._author = author
        self.__pages = pages
    
    def get_author(self):
        return self._author
    
    def get_pages(self):
        return self.__pages
    
    def set_author(self, author):
        self._author = author
        return self
    
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
            return self
        else:
            raise ValueError('Количество страниц должно быть больше нуля')
        
    def display_info(self):
        return f"Название: '{self.title}', автор: '{self._author}', кол-во страниц: '{self.__pages}'"