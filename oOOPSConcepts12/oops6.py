# Inheritance
#import oops7  # doubt needed clarification
#obj1 = oops7.Employee()
#obj2 = oops7.Person()
#print(obj1.yob)

#from oops7 import Employee # importing single class when multiple classes exist in file

# import util.util1 # one way
from util.util1 import Person3
obj3 = Person3("alekhya","k",1994)
print("from person3",obj3.yob)
class Person1:
# declaring variables directly in the class
    _name = "sri"
    __surname = "kuchipudi"
    yob = 1991
obj = Person1()
print(obj)
# employee is child class , person is parent class
class Employee(Person1): # Inheritance -> used to inherit the properties of other class

    pass
obj1 = Employee()
print(obj1.yob)
print(obj1._name)
print(obj1._Person1__surname)





