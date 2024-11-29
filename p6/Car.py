from datetime import date
class Car:
    def __init__(self, model):
        self.model = model
        self._year = None
        self.__mileage = None

    def get_year(self):
        return self._year
    
    def get_mileage(self):
        return self.__mileage
    
    def set_year(self, year):
        if (1886 <= year <= date.today().year):
            self._year = year
            return self
        else:
            raise ValueError('value_error')
        
    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
            return self
        else:
            raise ValueError('value_error')

    

