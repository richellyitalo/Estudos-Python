# ESCRITA MÚLTIPLA
# file = open('_file.dat', 'a')

# file.writelines(('0123456789', '\n', 'abcdefghijklmnopqrstuvxyz'))

# Dividindo o texto e escrevendo em múltiplas linhas
# textos = 'Eu quero esse texto completamente dividio em linhas'
#
# file.writelines('\n'.join(textos.split(' ')))

# file.close()

# -------------------------------------------

# LEITURA
file = open('_file.dat', 'r')

# leitura de qtd carateres definido
print(file.read(5))

print(file.read(3))

# leitura de linha
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline(15))
print(file.readline(3))

file.close()

print('***** readlines *****')
file = open('_file.dat', 'r')

lines = file.readlines()
file.close()
for line in lines:
    print(line)

print('***** lendo enquanto tiver linha ******')
file = open('_file.dat', 'r')

while True:
    line = file.readline()
    if not line:
        print('fim')
        break
    print(line, end='')

file.close()

