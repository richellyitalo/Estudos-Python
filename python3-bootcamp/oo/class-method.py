class Pessoa:
    usuarios_ativos = 0

    @classmethod
    def mostrar_ativos(cls, msg='nada'):
        return str(cls.usuarios_ativos) + msg
        
    def __init__(self):
        Pessoa.usuarios_ativos += 1
        
    def ativar_usuario(self):
        Pessoa.usuarios_ativos += 1


ser1 = Pessoa()
ser2 = Pessoa()
print(ser2.mostrar_ativos())

print(Pessoa.mostrar_ativos('cuzao'))
