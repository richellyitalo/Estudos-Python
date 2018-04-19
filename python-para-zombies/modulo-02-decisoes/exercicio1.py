velocidade = int(input('Velocidade: '))
if (velocidade > 100):
    print ("Você foi multado")
    multa = (velocidade-110) * 5
    print ('Valor da multa é R$ %5.2f' %multa)
