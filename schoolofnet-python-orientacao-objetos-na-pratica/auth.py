from cash_machine import accounts
from cash_machine import BankAccount


class AuthBankAcount:
    bank_accounted_authenticated = None

    @staticmethod
    def authenticate(account_number, password):
        for account in accounts:
            if AuthBankAcount.__has_bank_account_valid(account, account_number, password):
                AuthBankAcount.bank_accounted_authenticated = account
                return account
        return False

    @staticmethod
    def __has_bank_account_valid(bank_account: BankAccount, account_number, password):
        return bank_account.check_account_number(account_number) and \
               bank_account.check_password(password)
