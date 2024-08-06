class Inueron:

    __students = "data science" # private variable

    def students(self):
        print("print class of students",self.__students)

i = Inueron()
i.students()
print(i._Inueron__students)
# we cannot access i.__students variable this is called data Abstraction
# If we are not going to allow the user to access data of class it is Abstraction
