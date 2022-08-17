import threading


class Account():
    def __init__(self) -> None:
        self._balance = 0

    def update(self, fee: float) -> None:
        new_balance = self._balance * (1 + fee);
        self._balance = new_balance
        print(f'New balance is: {self._balance}')
    
    def deposit(self, amount):
        self._balance += amount
        print(f'New balance is: {self._balance}')

class DepositOperation(threading.Thread):
    def __init__(self, account: Account, amount: float):
        super().__init__()
        self.account = account
        self.amount = amount

    def run(self):
        self.account.deposit(self.amount)

class UpdateOperation(threading.Thread):
    def __init__(self, account: Account, fee: float):
        super().__init__()
        self.account = account
        self.fee = fee

    def run(self):
        self.account.update(self.fee)


def Main() -> None:
    account = Account()
    deposit_op = DepositOperation(account, 100)
    update_op = UpdateOperation(account, 0.1)
    deposit_op.start()
    update_op.start()
    deposit_op.join()
    update_op.join()
    print(f'Final balance is: {account._balance}')

Main()