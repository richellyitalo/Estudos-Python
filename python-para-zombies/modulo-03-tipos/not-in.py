letras = []
vogais = 0
while True:
    letra = input("Informe uma letra: " )
    if letra == "0":
        break
    if letra in 'aeiou':
        letras.append(letra)
        vogais += 1
print("Total de %d" %vogais, letras)
