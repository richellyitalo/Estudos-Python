from utils import header, clear
from console import MachineConsole, AuthBankConsole


def main():
    clear()
    header()

    if AuthBankConsole.is_auth():
        clear()
        header()

        MachineConsole.call_operation()
    else:
        print('Não autenticado')


if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar...')
