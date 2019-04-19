# # OK
# from pac import pac1
# from pac.subpac1 import pac2
#
# print(pac1.lista)
# print(pac2.nome)

# OK
# from pac import pac1
#
# print(pac1.nome)

# OK
# from main import accounts
#
# print(accounts)

'''
def principal():
    import main
    print(main.accounts)

principal()

# não irá rodar
# está fora do escopo onde foi importado
print(main.accounts)
'''

import os
from bank_account_variables import money_slips, accounts

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# try:
#     file = open(BASE_PATH + '/_file.dat', 'a')
#
#     file.write('Hello')
#     file.write('\n')
#     file.write('World!')
# except Exception as e:
#     print('Deu pau')
#     print('CODIGO:', e)
# finally:
#     file.close()


def open_file_bank(mode):
    return open(os.path.join(BASE_PATH, '_file_bank.dat'), mode)


def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')


def write_accounts(file):
    for account, account_data in accounts.items():
        file.writelines((
            account, ';',
            account_data['name'], ';',
            account_data['password'], ';',
            str(account_data['value']), ';',
            str(account_data['admin']), ';',
            '\n'
        ))


def read_money_slips(file):
    line = file.readline()
    while line.find(';') is not -1:
        semicolon_pos = line.find(';')
        money_slip_block = line[0:semicolon_pos]
        set_block_money_slip(money_slip_block)
        if semicolon_pos + 1 == len(line):
            break
        else:
            line = line[semicolon_pos + 1:len(line)]


def read_accounts(file):
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for account_line in lines:
        extract_data_account(account_line)


def extract_data_account(account_line):
    account_data = []
    while account_line.find(';') is not -1:
        semicolon_pos = account_line.find(';')
        data = account_line[0:semicolon_pos]
        account_data.append(data)
        if semicolon_pos + 1 == len(account_line):
            break
        else:
            account_line = account_line[semicolon_pos + 1:len(account_line)]
    add_bank_account(account_data)


def add_bank_account(account_data):
    accounts[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'value': float(account_data[3]),
        'admin': bool(account_data[4])
    }


def set_block_money_slip(money_slip_block):
    equal_pos = money_slip_block.find('=')
    money_bill = money_slip_block[0:equal_pos]
    length_money_slip_block = len(money_slip_block)
    money_value = money_slip_block[equal_pos + 1:length_money_slip_block]
    # print(money_bill, money_value)
    money_slips[money_bill] = int(money_value)


def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()

    file = open_file_bank('r')
    read_accounts(file)
    file.close()


def save_money_slips():
    file = open_file_bank('r')
    lines = file.readlines()
    file.close()

    file = open_file_bank('w')
    lines[0] = ''
    for money_slip_type, value in money_slips.items():
        lines[0] += money_slip_type + '=' + str(value) + ';'
    lines[0] += '\n'

    file.writelines(lines)
    file.close()


def delete_file():
    file_path = os.path.join(BASE_PATH, '_file_delete.dat')
    file = open(file_path, 'w')
    file.close()
    if os.path.exists(file_path):
        os.unlink(file_path)
    else:
        print('[!] Arquivo não existe')