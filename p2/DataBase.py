from io import TextIOWrapper
import re
from UserScheme import UserScheme

class DataBase:

    users = []

    def getData(self, url):
        with open(url, 'r', encoding='UTF-8') as f:
            result = f.readlines()
            f.close()
            return result

    def serializers(self, data:TextIOWrapper):
        content = []
        for i in data:
            schema = dict()
            line = [i for i in re.split(r'\s', i) if i != '']
            for index in range(0 , len(line) - 1, 2):
                schema[line[index]] = line[index+1]
            content.append(schema)
        return content
        

    def createUser(self, data):
        for i in data:
            user = UserScheme()
            for key, item in i.items():
                setattr(user, key, item)
            self.users.append(user)
        return self.users
            
    def search(self, attr, keyWord):
        searchResult = []
        for obj in self.users: 
            if getattr(obj, attr, None) == keyWord:
                searchResult.append(obj)
        if (len(searchResult) > 0):
            return searchResult
        else:
            print('exception: Objects not found!!!')
            return searchResult