class Person4:
    def age(self,current_year,DOB):
        return current_year - DOB

    def take_emailID(self,emailID):
        print("take emailID from person",emailID)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        DOB = int(input("enter DOB"))
        return DOB

sri = Person4()
chait = Person4()
alekhya = Person4()
print(sri.age(2024,1994))
print(sri.ask_name())
print(sri.ask_dob())
sri.take_emailID("sri@gmail.com")


'''
task
for the past questions given on list,dict, tuple, set, string
try creating separate class for each one (list, tuple etc)
and restructure the code
1. use exception handling
2. use logging
3. use documentation
'''
