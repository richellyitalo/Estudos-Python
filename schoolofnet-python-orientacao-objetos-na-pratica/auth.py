from cash_machine import accounts
from cash_machine import BankAccount
from file import BankAccountFileReader


class AuthBankAcount:
    bank_accounted_authenticated = None

    @staticmethod
    def authenticate(account_number, password):
        bank_account_fr = BankAccountFileReader()
        bank_account = bank_account_fr.get_account(account_number)
        
        if bank_account and AuthBankAcount.__has_bank_account_valid(bank_account, account_number, password):
            AuthBankAcount.bank_accounted_authenticated = bank_account
            return bank_account
        return False

    @staticmethod
    def __has_bank_account_valid(bank_account: BankAccount, account_number, password):
        return bank_account.check_account_number(account_number) and \
               bank_account.check_password(password)
