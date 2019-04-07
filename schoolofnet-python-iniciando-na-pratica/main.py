from getpass import getpass
import os

clear = 'cls' if os.name == 'nt' else 'clear'

# contas e cédulas
accounts = {
    '0001-01': {
        'name': 'Fulano de tal',
        'password': '123',
        'value': 50,
        'admin': False
    },
    '0001-02': {
        'name': 'Beltrano de tal',
        'password': '123',
        'value': 150,
        'admin': False
    },
    '1111-11': {
        'name': 'Admin de tal',
        'password': '123',
        'value': 1000,
        'admin': True
    }
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5
}

while True:
    print('*********************************')
    print('**** Void - Caixa Eletrônico ****')
    print('*********************************')

    account_typed = input('Digita sua conta: ')
    password_typed = getpass('Informe a senha: ')

    '''
    # solução com tuplas - mais demorado o processamento
    accounts = [
        {
            'account': '0001-01',
            'name': 'Fulano de tal',
            'password': '123',
            'value': 0
        },
        {
            'account': '0001-02',
            'name': 'Beltrano de tal',
            'password': '123',
            'value': 0
        }
    ]
    
    flag = False
    for account in accounts:
        if account['account'] == account_typed and account['password'] == password_typed:
            flag = True
            print('[v] Conta válida')
    
    if not flag:
        print('[!] Conta inválida')
    
    '''

    if account_typed in accounts and password_typed == accounts[account_typed]['password']:
        os.system(clear)

        is_admin = accounts[account_typed]['admin']

        print('*********************************')
        print('**** Void - Caixa Eletrônico ****')
        print('*********************************')
        print('1 - Saldo')
        print('2 - Saque')
        print('10 - Incluir cédulas') if is_admin else None

        option_typed = input('Informe uma opção: ')

        if option_typed == '1':
            print('Seu saldo é %s' % accounts[account_typed]['value'])
        elif option_typed == '10' and is_admin:
            ammount_type = input('Informe a quantidade de cédulas: ')
            money_bill_typed = input('Informe a cédula a ser incluída: ')
            money_slips[money_bill_typed] += int(ammount_type)
            print(money_slips)
        elif option_typed == '2':
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

    else:
        print('[!] Dados inválidos')

    input('Pression <ENTER> para continuar...')

    os.system(clear)
