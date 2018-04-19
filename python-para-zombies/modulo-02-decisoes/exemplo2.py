minutos = int(input("Minutos: "))
if minutos < 200:
    preco = 0.20
elif minutos < 100:
    preco = 0.18
else:
    preco = 0.05

print("Preço diferencial: R$ %6.2f" %preco)
