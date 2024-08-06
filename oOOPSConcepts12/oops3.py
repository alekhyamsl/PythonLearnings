# if we are creating more that one constructor then python will consider second/latest one
class Person2:

    def __init__(self,name,surname,emailID,year_of_birth):
        self.name = name
        self.surname = surname
        self.emailID = emailID
        self.year_of_birth = year_of_birth

    def __init__(self,name,DOB):
        self.name = name
        self.DOB = DOB

sri_var = Person2("alekhya","kuchipudi","alekhyamslgmail.com",1994)