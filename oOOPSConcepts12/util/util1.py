class Person3:
    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

obj3 = Person3("chaitanya","k",1991)
print(obj3._name)