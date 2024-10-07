class Human:
    height = None
    age = None
    

hu1 = Human()
hu2 = Human()

print(hu1.age)
print(hu2.age)

hu1.age = 20
hu2.age = 22

print(hu1.age)
print(hu2.age)

hu1.height = 180
hu2.height = 185

delattr(hu1, 'height')
delattr(hu2, 'height')

print(hasattr(hu1, 'height'))
print(hasattr(hu2, 'height'))

hu1.name = 'Il\'ya'
print(hu1.name)

print('!')
delattr(hu2, 'age')
setattr(hu2, 'name', 'Ivan')
print(hasattr(hu2, 'age'))
print(getattr(hu2, 'name'))