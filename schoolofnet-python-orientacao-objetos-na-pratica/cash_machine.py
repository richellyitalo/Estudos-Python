from file import BankAccountFileWriter


class BankAccount:
    def __init__(self, account_number, name, password, value, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin

    def check_account_number(self, account_number):
        return self.account_number == account_number

    def check_password(self, password):
        return self.password == password

    def debit_balance(self, value):
        self.value -= value
        return self.value

    def __str__(self):
        return self.account_number + ' | ' + self.name


class CashMachineWithdraw:
    @staticmethod
    def withdraw(bank_account: BankAccount, value):
        from file import MoneySlipsFileWritter
        cash_machine = CashMachineGetter().get()
        money_slips_user = cash_machine.withdraw(value)
        if money_slips_user:
            CashMachineWithdraw.debit_balance(bank_account, value)
            MoneySlipsFileWritter().write_money_slips(cash_machine.money_slips)
        return cash_machine

    @staticmethod
    def debit_balance(bank_account, value):
        bank_account.debit_balance(value)
        BankAccountFileWriter().write_bank_account(bank_account)



class CashMachineInsertMoneyBill:
    @staticmethod
    def insert_money_bill(money_bill, amount):
        from file import MoneySlipsFileWritter
        cash_machine = CashMachineGetter().get()
        cash_machine.money_slips[money_bill] += amount
        MoneySlipsFileWritter().write_money_slips(cash_machine.money_slips)
        return cash_machine


class CashMachine:
    def __init__(self, money_slips):
        self.money_slips = money_slips
        self.money_slips_user = {}
        self.value_remaining = 0

    def withdraw(self, value):
        self.value_remaining = value

        self.__calculate_money_slips_user()

        if self.value_remaining == 0:
            self.__decrease_money_slips()
        return False if self.value_remaining != 0 else self.money_slips_user

    def __calculate_money_slips_user(self):
        for money_bill, money_bill_qtd in self.money_slips.items():
            money_bill_int = int(money_bill)
            if 0 < self.value_remaining // money_bill_int <= self.money_slips[money_bill]:
                self.money_slips_user[money_bill] = self.value_remaining // money_bill_int
                self.value_remaining = self.value_remaining - self.value_remaining // money_bill_int * money_bill_int

    def __decrease_money_slips(self):
        for money_bill in self.money_slips_user:
            self.money_slips[money_bill] -= self.money_slips_user[money_bill]

# Não está usando método estático pois é o padrão - Factory
# Tem o objetivo de trazer apenas o objeto 
# mantendo o construtor em um único lugar
class CashMachineGetter: 
    def get(self):
        from file import MoneySlipsFileReader
        money_slips = MoneySlipsFileReader().get_money_slips()
        return CashMachine(money_slips)


accounts = [
    BankAccount('0001-01', 'Fulano de tal', '123', 50, False),
    BankAccount('0001-02', 'Beltrano de tal', '123', 10, False),
    BankAccount('1111-01', 'Admin de tal', '123', 1000, True)
]
