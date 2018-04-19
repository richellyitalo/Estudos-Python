def embaralha(s):
    import random
    p = list(s)
    random.shuffle(p)
    return ''.join(p)
s = input('Digite uma palavra: ')
print(embaralha(s))
