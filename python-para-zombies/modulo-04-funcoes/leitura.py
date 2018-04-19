arquivo = open('arquivos.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()
