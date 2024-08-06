# In python both scripting and OOPS pattern of coding is allowed
# OOPS is way of writing code
"""
class
object
when we talk about Animal/Car we will be able to get some outline idea
but we dont know about the exact/precise type/Specification of Car/Animal
So class is a blueprint/virtualization of real world entity
or
classification of real world entity
Why we are talking about class in programming world
In software development we connect with various components
to maintain entire software/module we need classes so the user can go there and change the code
as required
Ex :
in one class we talk about DB connections
In next class we talk about API's
In other we talk about Logins
Reusability and maintenance of code is easy with OOPS
"""
"""
constructor : is a method by which you will be able to pass data to the class
"""

class Person:
    def __init__(self,name,surname,emailID,year_of_birth): # constructor, default inbuilt method
        # instead of self any keyword can be used as argument
        # self is not a keyword it is like a pointer to class
        # so self.name is pointed to class
        self.name1 = name
        self.surname = surname
        self.emailID = emailID
        self.year_of_birth = year_of_birth

alekhya_var = Person("alekhya","kuchipudi","alekhyamslgmail.com",1994)
chait_var = Person("chaitanya","kuchipudi","sri@gmail.com","1991")
# alekhya_var is variable of person class and is called the object(which is real world entity)
print(alekhya_var.name1)
print(alekhya_var.surname)
print(chait_var.name1)
print(chait_var.surname)
print(type(alekhya_var))
print(type(chait_var))




