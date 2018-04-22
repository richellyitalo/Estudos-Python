#para receber dicionars usa se **kwargs
def cores(**kwargs):
    for eng, br in kwargs.items():
        print(f'ingles: {eng} br: {br}')

cores(red='vermelho', blue='azul')
