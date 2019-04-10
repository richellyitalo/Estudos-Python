from bank_account_variables import accounts, money_slips
import utils
from getpass import getpass


def main():
    utils.header()

    account_auth = account_connect()

    if account_auth:
        utils.clear()

        utils.header()

        option_typed = get_menu_options_typed(account_auth)

        do_operation(option_typed, account_auth)

    else:
        print('[!] Dados inválidos')


def is_admin(account_auth):
    return accounts[account_auth]['admin']


def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    elif option_typed == '10' and is_admin(account_auth):
        deposit_money_slips()
    elif option_typed == '2':
        withdraw()


def show_balance(account_auth):
    print('Seu saldo é %s' % accounts[account_auth]['value'])


def deposit_money_slips():
    ammount_type = input('Informe a quantidade de cédulas: ')
    money_bill_typed = input('Informe a cédula a ser incluída: ')
    money_slips[money_bill_typed] += int(ammount_type)
    print(money_slips)


def withdraw():
    value_typed = input('Digite o valor a ser sacado: ')

    money_slips_user = {}
    value_int = int(value_typed)

    # if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
    if 0 < value_int // 100 <= money_slips['100']:
        money_slips_user['100'] = value_int // 100
        value_int = value_int - value_int // 100 * 100

    # if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
    if 0 < value_int // 50 <= money_slips['50']:
        money_slips_user['50'] = value_int // 50
        value_int = value_int - value_int // 50 * 50

    # if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
    if 0 < value_int // 20 <= money_slips['20']:
        money_slips_user['20'] = value_int // 20
        value_int = value_int - value_int // 20 * 20

    if value_int is not 0:
        print('O caixa não possui cédulas disponíveis!')
    else:
        for money_bill in money_slips_user:
            money_slips[money_bill] -= money_slips_user[money_bill]
        print('Retire as notas: ')
        print(money_slips_user)


def account_connect():
    account_typed = input('Digita sua conta: ')
    password_typed = getpass('Informe a senha: ')

    if account_typed in accounts and password_typed == accounts[account_typed]['password']:
        return account_typed
    else:
        return False


def get_menu_options_typed(account_auth):
    print('1 - Saldo')
    print('2 - Saque')
    print('10 - Incluir cédulas') if is_admin(account_auth) else None
    return input('Informe uma opção: ')
