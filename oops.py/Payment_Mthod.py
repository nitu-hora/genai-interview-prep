class PaymentMethod:
    def process(self, amount):
        raise NotImplementedError("Subclass must implement process")

    def validate(self):
        raise NotImplementedError("Subclass must implement validate")

    def __str__(self):
        raise NotImplementedError("Subclass must implement str")


class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiry, cvv):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
        self.__validated = False

    def validate(self):
        if len(str(self.card_number))!=16:
            raise ValueError("card number must be 16 digits")
        elif self.expiry == None:
            raise ValueError("Expiry cant be empty")
        elif len(str(self.cvv)) !=3:
            raise ValueError("cvv must be 3 digits")
        self.__validated = True

    def process(self, amount):
        if self.__validated == False:
            raise RuntimeError("card not validated")
        elif amount <= 0:
            raise ValueError("amount cant be 0")
        return f"Charged ${amount:.2f} to card ending {self.card_number[-4:]}"


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
        self.__validated = False

    def validate(self):
        if "@" not in self.email or "." not in self.email:
            raise ValueError("Email must have @ and .")
        self.__validated = True

    def process(self, amount):
        if self.__validated == False:
            raise RuntimeError("email not validated")
        return f"Sent ${amount:.2f} via PayPal to {self.email}"

class Crypto(PaymentMethod):
    def __init__(self, wallet_address, coin):
        self.wallet_address = wallet_address
        self.coin = coin
        self.__validated = False

    def validate(self):
        if len(str(self.wallet_address)) < 26:
            raise ValueError("address must be 26 digits")
        elif self.coin not in ["BTC", "ETH", "USDT"]:
            raise ValueError('coin must be one of these ["BTC", "ETH", "USDT"]')
        self.__validated = True

    def process(self,amount):
        if self.__validated == False:
            raise RuntimeError("address not validated")
        return f"Transferred {amount} {self.coin} to wallet {self.wallet_address[:6]}..."
        

def checkout(payment_method: list, amount: float):
    for payment in payment_method:
        try:
            payment.validate()
            result = payment.process(amount)
            print(result)
            return
        except (ValueError, RuntimeError) as e:
            print(e)

    print("All payment method failed")


methods = [
    CreditCard("1234", "12/26", "123"),               # invalid — not 16 digits
    PayPal("not-an-email"),                            # invalid — no @ or .
    CreditCard("1234567890123456", "12/26", "999"),    # valid
    Crypto("1A2B3C4D5E6F7G8H9I", "DOGE"),             # invalid coin
]

checkout(methods, 99.99)

        
       