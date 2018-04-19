palavra = input('Palavra: ')
i = 0
while i < len(palavra):
    if palavra[i] in 'aeiou':
        palavra = palavra[:i] + '*' + palavra[i + 1:]
    i += 1
print ('Palavra final', palavra)
