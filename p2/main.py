from DataBase import DataBase

db = DataBase()

data = db.getData('data.txt')

serialize = db.serializers(data)

db.createUser(serialize)

for item in db.users:
    print(item.__dict__)


search = db.search('name', 'Dmitriy')

for i in search:
    print(i.__dict__)