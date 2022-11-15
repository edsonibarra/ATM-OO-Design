from account import Account


class CheckingAccount(Account):
    def __init__(self, debit_card_number):
        
        self.__debit_card_number = debit_card_number
