meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
data = input('Data (dd/mm/yyyy): ')
dia, mes, ano = data.split('/')
mesExtenso = meses[int(mes) - 1]
print ('%s de %s de %s' % (dia, mesExtenso, ano))

