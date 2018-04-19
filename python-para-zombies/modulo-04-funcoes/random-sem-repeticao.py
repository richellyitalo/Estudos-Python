lista = []
while len(lista) < 15:
    import random
    num = random.randint(10, 100)
    if num not in lista:
        lista.append(num)
lista.sort()
print (lista)
