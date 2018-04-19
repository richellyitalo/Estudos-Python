def fat(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f
valor = int(input('Numero para fatorar: '))
print (fat(valor))
