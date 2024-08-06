class Car:

    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def milage(self):
        print("milage of this car")

class Tata(Car):
    pass

c = Car("solid1","v8","radial1")
print(c)

t = Tata("solid","v6","radial") # as Tata class inherits Car class even if constructor is not defined in
# Tata class but defined in its Parent Car class while creating object we have to pass the arguments
print(t)
print(t.milage())




