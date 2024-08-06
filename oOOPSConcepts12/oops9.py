# Types of Inheritance
# single Inheritance
# Multiple Inheritance
# multi level Inheritance

class Bank:

    def transaction(self):
        print("Total transaction value")

    def accountOpening(self):
        print("This will show your account opening status")

    def deposit(self):
        print("This will show deposit amount")

class Hdfc_Bank(Bank):

    def hdfc_to_icici(self):
        print("this will show transaction amount from hdfc to icici")

class Icici(Hdfc_Bank): #now this class have access to all methods of Bank and Hdfc_Bank classes
    pass                # this is multi level inheritance example

ic = Icici()
ic.hdfc_to_icici()
ic.deposit()
ic.transaction()
ic.accountOpening()


