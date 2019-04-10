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
from bank_account_variables import money_slips


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


# 100=9;50=7;20=3;
def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')
