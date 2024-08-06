# to restrict access of variable we different levels of access
# public -> by default the declared variables are public
# private -> if variable is defined with __ it is private variable
# protected -> if variable name is starting with _ is protected variable
# In python it's just a notation used for declaring private, protected variables
# as per python creator there is no real public, private, protected variables but they do exist

class Person:
    def __init__(self,name,surname,year_of_birth):
        # self.name is class variable
        self._name = name
        self.__surname = surname
        self.year_of_birth = year_of_birth

sri = Person("chaitanya","kuchipudi",1991)
print(sri._name)
# print(sri.__surname) this gives an error as it is private variable and cannot accessed outside declared method
print(sri._Person__surname) # to call private varaible

