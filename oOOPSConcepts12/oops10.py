# This is example of multiple Inheritance
class Bank:

    def transaction(self):
        print("Total transaction value")

    def accountOpening(self):
        print("This will show your account opening status")

    def deposit(self):
        print("This will show deposit amount")

    def test(self):
        print("This is test method from Bank class")

class Hdfc_Bank:

    def hdfc_to_icici(self):
        print("this will show transaction amount from hdfc to icici")

    def test(self):
        print("This is test method from Hdfc Bank")

class Icici_Bank(Hdfc_Bank,Bank):
    pass

class inueron_Bank:
    def account_status_icici(self):
        print("account status from ICICI")

class Aixs(Bank,Hdfc_Bank,inueron_Bank):
    pass



i = Icici_Bank()
i.deposit()
i.hdfc_to_icici()
i.accountOpening()
i.transaction()
i.test() # it chooses the method from class which is mentioned in First argument while Inheritance
a = Aixs()
a.test()
a.transaction()
a.hdfc_to_icici()
a.deposit()
a.accountOpening()
a.account_status_icici()