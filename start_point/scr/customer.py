class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reducing_wallet (self, cash):
        self.wallet -= cash

