class Goods:
    title = 'Ice Cream'
    weight = 100
    type = 'Food'
    price = 150

class Car:
    model = 'Toyota'
    color = 'black'
    number = 'P340AH123'

carObj = Car()

carObj.model = 'fooBar'

print(carObj.color)
print(carObj.__dict__)

# __dict__ хранит присвоенные экземпляру класса(объекту) атрибуты.
