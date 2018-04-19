a = 5
def muda_interna():
    global a
    a = 10
print ('antes de mudar', a)
muda_interna()
print ('depois de mudar ', a)
