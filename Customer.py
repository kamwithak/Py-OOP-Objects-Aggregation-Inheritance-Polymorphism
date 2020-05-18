from AccountManagementSystem import SavingsAccount, CheckingAccount
class Customer:
    def __init__(self, nameOfCustomer, dateOpened, phone):
        self.name = nameOfCustomer
        self.dateOpened = dateOpened
        self.phone = phone
        self.accounts = [CheckingAccount(self.name, self.dateOpened, 0), SavingsAccount(self.name, self.dateOpened, 0)]

    def getName(self):
        return self.name
    def getDateOpened(self):
        return self.dateOpened
    def getPhoneNumber(self):
        return self.phone
    
    def printName(self):
        print(self.name)
