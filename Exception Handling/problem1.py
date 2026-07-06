class InsufficientBalance(Exception):
    pass
class WithdrawlLimit(Exception):
    pass
class InvalidInput(Exception):
    pass

class ATM:
    def __init__(self,balance):
        self.balance = balance
        
    def withdraw(self,amount):
        try:
            if amount <= 0:
                raise InvalidInput("No negative")
            if amount > 25000:
                raise WithdrawlLimit("No more than 25000")
            if amount > self.balance:
                raise InsufficientBalance("Insufficient balance")
            
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")

        except InvalidInput as e:
            print(e)

        except WithdrawlLimit as e:
            print(e)

        except InsufficientBalance as e:
            print(e)
            
atm = ATM(10000)

atm.withdraw(-500)     # Amount must be greater than 0
atm.withdraw(30000)    # Cannot withdraw more than 25000
atm.withdraw(15000)    # Insufficient balance
atm.withdraw(5000)     # Withdrawal successful. Remaining balance: 5000