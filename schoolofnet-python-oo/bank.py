class Account1(object):
    def __init__(self, number):
        self.number = number
        self.__total = 0
        self.teste = 'Teste'
        self.__teste()

    def deposit(self, value):
        self.__total += value
    
    def withdraw(self, value):
        self.__total -= value
        self.__total -= 1

    def get_total(self):
        return self.__total
    
    def __teste(self):
        print('Teste')

    def __metodo_privado(self):
        print('Método privado acessando atributos privado do objeto: ' + str(self.number))


class Account2(Account1):
    def __init__(self, number, cvv):
        # super(Account2, self).__init__(number)
        super().__init__(number)
        self.cvv = cvv

    def withdraw(self, value):
        print(self.teste)
        self._Account1__total -= value
        self._Account1__total -= 5

        # Acessando método publico
        print(self.get_total())

        # Acessando método privado
        self._Account1__metodo_privado()
    
    def get_total(self):
        print('Total do método Account2 %s', self._Account1__total)
        return self._Account1__total
