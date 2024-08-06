# Encapsulation

class Inueron:

    def __init__(self):
        self.student = "data science"

    def students(self):
        print(self.student)

i = Inueron()
i.students() # prints data analytics
i.student = "data analytics"
i.students() # prints data analytics
# here we are trying to override the value of variable at run time
print("__________")
# Encapsulation -> if you do not allow the user to modify the data directly it is encapsulation
# here we are not allowed to change the value of private variable directly
# but we are allowing the user to change the value using the method indirectly
# here the concept of getters and setters will come
# when value of private variable is set by function it is setter

class Inueron1:

    def __init__(self):
        self.__student = "data science"

    def students(self):
        print(self.__student)

    def students_change(self,new_value):
        self.__student = new_value

i1 = Inueron1()
i1.students()
i1.__student = "Big data"
i1.students() # here it is not overriding the value of private variable to Big data
i1.students_change("Artificial Intelligence")
i1.students() # now here the value of private variable(__student) is changed by using method in the class

"""
difference b/w Abstraction and Encapsulation
If we are not able to access data directly it is data hiding/Abstraction
In encapsulation we are not allowing user to modify data directly 
but allowing to modify them indrectly using method
"""
