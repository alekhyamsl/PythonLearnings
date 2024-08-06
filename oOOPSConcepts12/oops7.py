# Inheritance
# packages are folders
# modules are files
# different classes exist in modules
import oops6 # the code in oops6.py file is imported to oops7.py file
print(oops6)
obj2 = oops6.Person1()
print(obj2.yob)
print(obj2._name)
print(obj2._Person1__surname)
print("______________")
class Person:
# declaring variables directly in the class
    _name = "sri"
    __surname = "kuchipudi"
    yob = 1991

    def _age(self,current_year): # protected function
        return current_year - self.yob
    def __age1(self,current_year): # private function
        return  current_year - self.yob

obj1 = Person()
print(obj1._age(2024))
print(obj1._Person__age1(2024))
class Employee(Person):
# declaring variables directly in the class
    _name = "alekhya"
    __surname = "k"
    yob = 1994

obj = Employee()
print(obj.yob) # prints value from Employee class
print(obj._name) # prints value from Employee class
print(obj._Person__surname) # prints value from Person1 class
print(obj._Employee__surname) #prints value from Employee class
print(obj._age(2024))
print(obj._Person__age1(2024))

