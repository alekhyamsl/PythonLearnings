# Example of method overriding
class Inueron:

    def student(self):
        print("details of all students")

    def achievers(self):
        print("print list of all achievers")

    def hallOfFame(self):
        print("print everyone from hall of fame")

class Inueron_vision(Inueron):

    def student(self): # method overriding
        print("prints student details from only inueron vision")

iv = Inueron_vision()
iv.student() # overrides the parent class method and executes child class method
