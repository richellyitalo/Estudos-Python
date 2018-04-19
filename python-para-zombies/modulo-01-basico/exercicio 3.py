dias = int(input('Dias: ' ))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
totalSegundos = 0
totalSegundos += segundos
totalSegundos += (minutos * 60)
totalSegundos += (horas * 60 * 60)
totalSegundos += (dias * 24 * 60 * 60)
print ('Total em segundos ', totalSegundos)
