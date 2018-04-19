salario = int(input('Salario: '))
porcentagem = int(input('Porcentagem: '))
aumento = salario * (porcentagem/100)
novoSalario = salario + aumento
print('o aumento de %.2f com novo salario %d' % (aumento, novoSalario))
