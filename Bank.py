from Customer import Customer
class Bank:
    def __init__(self, nameOfBank, listOfCustomers=[]):
        self.nameOfBank = nameOfBank
        self.listOfCustomers = listOfCustomers
    
    def addCustomer(self, aCustomer):
        self.listOfCustomers.append(aCustomer)
    
    def printBankName(self):
        print(self.nameOfBank)


if __name__ == "__main__":
    myBank = Bank("TD-Canada-Trust")
    myFirstCustomer = Customer("Joe", "05/18/20", "012-345-6789")
    print(myFirstCustomer.accounts[1].interestRate)
    myBank.addCustomer(myFirstCustomer)