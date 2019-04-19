import operations
import utils
from file import load_bank_data
from bank_account_variables import accounts


def main():
    load_bank_data()

    print(accounts)
    operations.main()

    input('Pressione <ENTER> para continuar...')

    utils.clear()


if __name__ == '__main__':
    while True:
        main()
