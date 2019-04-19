from getpass import getpass
from auth import AuthBankAcount
from cash_machine import CashMachine, CashMachineWithdraw


class AuthBankConsole:
    @staticmethod
    def is_auth():
        account_number = input('Digite sua conta: ')
        password = getpass('Informe a senha: ')
        return AuthBankAcount.authenticate(account_number, password)


class MachineConsole:
    @staticmethod
    def call_operation():
        option_typed = MachineConsole.__get_option_typed()
        MachineOperation.do_operation(option_typed)

    @staticmethod
    def __get_option_typed():
        print('%s - Saldo' % MachineOperation.OPERATION_SHOW_BALANCE)
        print('%s - Saque' % MachineOperation.OPERATION_WITHDRAW)
        return input('Informe uma opção: ')


class MachineOperation:
    OPERATION_SHOW_BALANCE = '1'
    OPERATION_WITHDRAW = '2'

    @staticmethod
    def do_operation(option):
        if option is MachineOperation.OPERATION_SHOW_BALANCE:
            ShowBalanceOperation.do_operation()
        elif option is MachineOperation.OPERATION_WITHDRAW:
            WithdrawOperation.do_operation()


class ShowBalanceOperation:
    @staticmethod
    def do_operation():
        bank_account = AuthBankAcount.bank_accounted_authenticated
        print('Saldo em conta: %s' % bank_account.value)


class WithdrawOperation:
    @staticmethod
    def do_operation():
        value_typed = input('Digite o valor a ser sacado: ')
        value_int = int(value_typed)
        bank_account = AuthBankAcount.bank_accounted_authenticated

        cash_machine = CashMachineWithdraw.withdraw(bank_account, value_int)
        if cash_machine.value_remaining != 0:
            print('Caixa não possui cédulas disponíveis')
        else:
            print('Pegue as notas no slot:')
            print(cash_machine.money_slips_user)
            print(vars(bank_account))
