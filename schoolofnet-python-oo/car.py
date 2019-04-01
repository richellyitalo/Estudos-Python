class Car:
    comum = 'Pneus'

    def __init__(self, name, maker, year):
        self.name = name
        self.maker = maker
        self.year = year
        self.color = 'Silver'
        # print('Instância de carro criada')

    def on(self):
        print('Atributo comum da classe: ' + self.comum)
        print(self.name + ' foi ligado.')

    @staticmethod
    def hello(x):
        print(x + ' : Parametro passado')

    @classmethod
    def show(cls):
        # não irá funcionar, pois o name pertence ao objeto
        # print(cls.name)

        print(cls.comum)

    @property
    def vencimento(self):
        return self.year + 1
