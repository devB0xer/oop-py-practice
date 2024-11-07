# 2. Создайте класс Employee, который будет представлять сотрудника и иметь
# следующие функции:
    # 1. Статический метод is_valid_age, который принимает возраст сотрудника и
    # проверяет, находится ли возраст в допустимом диапазоне (например, от 18 до
    # 65 лет).
    
    # 2. Метод класса from_string, который принимает строку с данными сотрудника в
    # формате "Имя, Возраст, Должность" и создает экземпляр класса Employee,
    # если возраст является допустимым. В противном случае метод должен
    # выбросить исключение ValueError.
    
    # 3. Метод экземпляра get_details, который возвращает строку с информацией о
    # сотруднике (например, "Имя: Иван, Возраст: 30, Должность: Менеджер")

class Employee:
    
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
    
    @staticmethod
    def isValidAge(age):
        return (18 <= age <= 65)
    
    @classmethod
    def fromString(cls, str):
        # str = "Имя, Возраст, Должность"
        data = str.split(', ')
        name = data[0]
        age = int(data[1])
        position = data[2]
         
        if (cls.isValidAge(age)):
            return cls(name, age, position)
        else:
            print('value error! age not valid')
            return False
            
    def getDetails(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}"
            
    
         
        