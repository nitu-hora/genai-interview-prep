# def fetch_data(url):
#     if "invalid" in url:
#         raise ValueError("Invalid URL format")
#     if "timeout" in url:
#         raise ConnectionError("Request timed out")
#     return {"data": "success"}


# def call_api(url):
#     result = None          # start as None
#     try:
#         result = fetch_data(url)  # call fetch_data here
#     except ValueError as e:
#         print(f"bad url : {e}")     # print "Bad URL: <error>"
#     except ConnectionError as e:
#         print(f"network error : {e}")     # print "Network error: <error>"
#     finally:
#         print("request attempt finished")     # always prints this
#     return result          # outside finally — return result


# # test
# print(call_api("https://good-url.com"))
# print(call_api("https://invalid-url.com"))
# print(call_api("https://timeout-url.com"))


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is insufficient for withdrawal of {amount}")

class InvalidCardError(Exception):
    def __init__(self, card_number, reason):
        self.card_number = card_number
        self.reason = reason
        super().__init__(f"card number {self.card_number} is invalid")

def process_payment(balance, amount, card_number):
    if card_number[0] not in "45":
        raise InvalidCardError(card_number, "must start with 4 or 5")
    elif amount > balance:
        raise InsufficientFundsError(balance, amount)
    return f"payment of {amount} succesfful. remaining balance : {balance - amount}"
    


test_cases = [
    (1000, 500, "4111111111111111"),   # valid card, enough balance
    (1000, 1500, "5200000000000000"),  # valid card, not enough balance
    (1000, 500, "9999999999999999"),   # invalid card
]

for balance, amount, card in test_cases:
    try:
        print(process_payment(balance, amount, card))
    except InsufficientFundsError as e:
        print(f"Payment failed: {e}")
    except InvalidCardError as e:
        print(f"Card rejected: {e}")



class DatabaseConnection:
    def __init__(self):
        self.connected = False

    def __enter__(self):
        print("opening DB connection")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing DB connection")
        self.connected = False

    def query(self,sql):
        if not self.connected:
            raise RuntimeError("No active connection")

        print(f"Running query: {sql}")

# Use inside the with block
with DatabaseConnection() as db:
    db.query("SELECT * FROM users")
    db.query("SELECT * FROM orders")

# Try using it outside the with block
db.query("SELECT * FROM products")