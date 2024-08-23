# Polymorphism
class Inueron:
    def students(self):
        print("print student details")

class Class_type:
    def students(self):
        print("print details of student class type")

def inueron_external(a):
    a.students()

i = Inueron()
inueron_external(i)
j = Class_type()
inueron_external(j)


def test(a,b):
    return a+b

print(test(5,6)) # one function but 2 different behaviours
print(test("alekhya","chaitanya"))

"""
topics discussed
class
object
constructor
inheritance
private
public
protected
abstraction
encaptulations
polymorpsim
package
modules
method overrridding

task:

For all the concepts that we have discussed in our class point by point you have to write
atleast 10 examples

you have to make sure that use ineuron studnets , class , class type , number of courses
, affiliates , blog, internship , jobs as a reference example


download sql workbench
search Mysql Workbench download in google
select OS -> Go to download page
download the second one 
Click on No thanks Just start my download link
while completing th wizard
select full 



root password : 

Why SQL(DB) in Data science?
Client will not give data in excel sheet or available in local system
then we have to connect to DB to fetch Data


root user have all CRUD permissions



"""