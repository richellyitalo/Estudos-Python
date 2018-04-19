arquivo = open('mensagem.txt', 'r')
texto = ''
for linha in arquivo.readlines():
    i = 0
    for letra in linha:
        if letra in 'aeiout':
            letra = '*' # novo.write('*')
        texto += letra
arquivo.close()
novo = open('crypto.txt', 'w')
novo.write(texto)
novo.close()
