class Translator:
    
    dictionary = {}

    def add(self, eng, rus):
        eng = eng.lower()
        rus = rus.lower()

        if not (eng in self.dictionary):
            self.dictionary[eng] = []
            self.dictionary[eng].append(rus)
        else:
            self.dictionary[eng].append(rus)

        return self.dictionary[eng]

    def remove(self, eng):
        eng = eng.lower()
        self.dictionary.pop(eng)

    def translate(self, eng):
        eng = eng.lower()
        return self.dictionary[eng][0]


foo = Translator()

foo.add('pizza', 'пицца')
foo.add('pizza', 'лепешка с овощами')

foo.add('car', 'машина')

print(foo.translate('pizza'))

foo.remove('pizza')

print(foo.dictionary)