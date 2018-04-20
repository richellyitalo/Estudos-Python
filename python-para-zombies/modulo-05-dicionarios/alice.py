arq = open('alice.txt', 'r', encoding='utf-8')
text = arq.read()
text = text.lower()
import string
for c in string.punctuation:
    text = text.replace(c, ' ')
text = text.split()

dic = {}
for p in text:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print('Alice apareceu %s vezes' %dic['alice'])
arq.close()
