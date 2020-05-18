''' Abstract '''
class Account(object):
    def __init__(self, accountHolder, dateOpened, balance):
        if type(self) is Account:
            raise Exception('Account is an abstract class and cannot be instantiated directly')
        self.accountHolder = accountHolder
        self.dateOpened = dateOpened
        self.accountBalance = balance

    def makeDeposit(self, amount):
        raise NotImplementedError

    def makeWithdrawal(self, amount):
        raise NotImplementedError


class SavingsAccount(Account):
    interestRate = 1.0
    def __init__(self, accountHolder, dateOpened, accountBalance, ir=1.0):
        super().__init__(accountHolder, dateOpened, accountBalance)
        self.interestRate = ir
    
    def makeDeposit(self, amount):
        pass
    def makeWithdrawal(self, amount):
        pass
    def calculateInterest(self):
        pass

class CheckingAccount(Account):
    def __init__(self, accountHolder, dateOpened, accountBalance, checkStyle='', minimumBalance=0):
        super().__init__(accountHolder, dateOpened, accountBalance)
        self.checkStyle = checkStyle
        self.minimumBalance = minimumBalance
    
    def makeDeposit(self, amount):
        pass
    def makeWithdrawal(self, amount):
        pass
    def calculateInterest(self):
        pass

