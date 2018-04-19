p = input('Palavra: ')

pInv = p[::-1]
if p == pInv:
    print('È palindrome')
else:
    print('não é palindrome')
