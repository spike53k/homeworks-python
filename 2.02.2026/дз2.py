class GameBank:
    def __init__(self, balance = 0):
        self._balance = balance
        self.__log = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction(amount)
            print(f"баланс: {self._balance}")
        else:
            print("ошибка")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self.__log_transaction(amount)
            print(f"баланс: {self._balance}")
        else:
            print("ошибка")

    def __log_transaction(self, operation):
        self.__log.append(operation)

bank = GameBank(30)
bank.deposit(50)
bank.withdraw(20)