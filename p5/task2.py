from Employee import Employee

print(Employee.isValidAge(17))
print(Employee.isValidAge(18))
print(Employee.isValidAge(65))
print(Employee.isValidAge(66))

employee = Employee.fromString('Иван, 30, менеджер')
employee2 = Employee.fromString('Вовка, 17, ну Вовка аче?)')

print(employee.getDetails())
print(employee2.getDetails())