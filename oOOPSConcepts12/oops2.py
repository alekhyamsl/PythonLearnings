class Person1:
    def __init__(sri,name,DOB):
        sri.name = name
        sri.DOB = DOB
    def age(sri,current_year):
        return current_year - sri.DOB

alekhya_var = Person1("alekhya",1994)
chait_var = Person1("chaitanya",1991)
# alekhya_var is variable of person class and is called the object(which is real world entity)
print(alekhya_var.name)
print(alekhya_var.DOB)
print(chait_var.name)
print(chait_var.DOB)
print(alekhya_var.name + str(alekhya_var.DOB))
print(chait_var.age(2024))

