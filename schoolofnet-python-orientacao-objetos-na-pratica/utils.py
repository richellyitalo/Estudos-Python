import os


def header():
    print('*********************************')
    print('**** Void - Caixa Eletrônico ****')
    print('*********************************')


def clear():
    clear_command = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_command)
