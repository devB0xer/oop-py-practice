from Resource import Resource

r1 = Resource('Connection1', 'connect to database')
r2 = Resource('Connection2', 'connect to database')

print(r1.name, '|', r1.resource_type)

for _ in range(1, 6):
    if _ == 3:
        del r2
    else:
        print(_)

