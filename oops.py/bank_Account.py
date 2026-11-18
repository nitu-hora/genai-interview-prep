class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = pin
        self.history =[]

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        self.history.append(f"Deposited {amount} | Balance: {self._balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            raise ValueError("Incorrect PIN")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount
        self.history.append(f"Withdrew {amount} | Balance: {self._balance}")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            raise ValueError("Incorrect PIN")
        if len(str(new_pin)) < 4:
            raise ValueError("New PIN must be at least 4 digits")
        self.__pin = new_pin

    def show_history(self):
        for entry in self.history:
            print(entry)

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @classmethod
    def from_dict(cls, data):
        return cls(data["account_holder"], data["balance"], data.get("pin", 0000))


# --- Test it ---
# acc = BankAccount("Nitu", 1000, 1234)

# print(acc.balance)          # 1000
# acc.deposit(500)
# print(acc.balance)          # 1500
# acc.withdraw(200, 1234)
# print(acc.balance)          # 1300
# acc.change_pin(1234, 9999)
# print("PIN changed")

# # These should raise errors:
# try:
#     acc.withdraw(100, 1234)     # old pin — should fail
# except ValueError as e:
#     print(f"Error: {e}")

# try:
#     acc.deposit(-50)            # negative amount — should fail
# except ValueError as e:
#     print(f"Error: {e}")

# try:
#     print(acc.__pin)            # name mangling — should fail
# except AttributeError as e:
#     print(f"Error: {e}")

# print(acc._BankAccount__pin)    # works — mangled name directly


# acc.deposit(500)
# try:
#     acc.withdraw(100, 1234)     # old pin — should fail
# except ValueError as e:
#     print(f"Error: {e}")
# acc.show_history()


# expected usage:
BankAccount.validate_amount(500)   # True
BankAccount.validate_amount(-10)   # False
acc = BankAccount.from_dict({"owner": "Nitu", "balance": 5000})
print(acc.owner, acc.balance)      # Nitu 5000