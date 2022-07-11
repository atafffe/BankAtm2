class main(object):
    def __init__(self, balance, withdrawl):
        self.balance = balance
        self.withdrawl = withdrawl
    def GetBalance(self):
        print("Balance was checked")
    def Withdraw(self):
        print("Withdrew some cash")

info = main(650, 300)
print("Balance: ", info.balance)
print("Withdrawn: ", info.withdrawl)