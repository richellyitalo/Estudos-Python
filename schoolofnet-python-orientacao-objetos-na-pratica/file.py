import os
import ast


class BankFile:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self._file = None

    def _open_file(self, mode):
        return open(os.path.join(BankFile.BASE_PATH, '_file_bank.dat'), mode)
        
    def _readlines(self):
        self._file = self._open_file('r')
        lines = self._file.readlines()
        self._file.close()
        return lines

    def _writelines(self, lines):
        self._file = self._open_file('w')
        self._file.writelines(lines)
        self._file.close()


class BankAccountFileReader(BankFile):
    def get_line_index_of_bank_account(self, account_number):
        lines = self._readlines()
        lines = self.__skip_first_line(lines)
        line_index = -1
        for index, line in enumerate(lines):
            bank_account_created = self.__create_bank_account_from_file_line(line)
            if bank_account_created.check_account_number(account_number):
                line_index = index
                break
        
        return line_index + 1

    def get_account(self, account_number):
        lines = self._readlines()
        lines = self.__skip_first_line(lines)
        bank_account = None
        for line in lines:
            bank_account_created = self.__create_bank_account_from_file_line(line)
            if bank_account_created.check_account_number(account_number):
                bank_account = bank_account_created
                break
        return bank_account
    
    def __skip_first_line(self, lines):
        return lines[1:len(lines)]

    def __create_bank_account_from_file_line(self, line):
        from cash_machine import BankAccount
        account_data = line.split(';')
        return BankAccount(
            account_data[0],
            account_data[1],
            account_data[2],
            float(account_data[3]),
            ast.literal_eval(account_data[4])
        )


class BankAccountFileWriter(BankFile):
    def write_bank_account(self, bank_account):
        line_index_to_update = BankAccountFileReader()\
            .get_line_index_of_bank_account(bank_account.account_number)
        lines = self._readlines()
        lines[line_index_to_update] = self.__format_line_to_write(bank_account)
        self._writelines(lines)

    def __format_line_to_write(self, bank_account):
        line = '%s;%s;%s;%s;%s;' % (
            bank_account.account_number,
            bank_account.name,
            bank_account.password,
            str(bank_account.value),
            str(bank_account.admin)
        )
        return line + '\n'

class MoneySlipsFile(BankFile):
    MONEY_SLIPS_LINE = 0


class MoneySlipsFileReader(MoneySlipsFile):
    def __init__(self):
        super().__init__()
        self.__money_slips = {}

    def get_money_slips(self):
        self._file = self._open_file('r')
        line_money_slips_to_read = MoneySlipsFile.MONEY_SLIPS_LINE
        line = self._file.readlines(line_money_slips_to_read)[0]
        while self.__has_semicolon(line):
            semicolon_pos = line.find(';')
            money_slip_block = line[0:semicolon_pos]
            self.__add_money_slips_from_file(money_slip_block)
            if self.__has_not_money_bill_to_read(semicolon_pos, line):
                break
            else:
                line = line[semicolon_pos + 1:len(line)]
        
        return self.__money_slips
    
    def __has_semicolon(self, line):
        return line.find(';') is not -1

    def __has_not_money_bill_to_read(self, semicolon_pos, line):
        return semicolon_pos + 1 == len(line)
    
    def __add_money_slips_from_file(self, money_bill_value):
        equal_pos = money_bill_value.find('=')
        money_bill = money_bill_value[0:equal_pos]
        length_money_bill_value = len(money_bill_value)
        money_value = money_bill_value[equal_pos + 1:length_money_bill_value]
        self.__money_slips[money_bill] = int(money_value)


class MoneySlipsFileWritter(MoneySlipsFile):
    def write_money_slips(self, money_slips):
        lines = self._readlines()
        line_to_write = MoneySlipsFile.MONEY_SLIPS_LINE
        lines[line_to_write] = self.__format_line_to_write(money_slips)
        self._writelines(lines)

    def __format_line_to_write(self, money_slips):
        line = ''
        for money_bill, money_value in money_slips.items():
            line += money_bill + '=' + str(money_value) + ';'
        return line + '\n'