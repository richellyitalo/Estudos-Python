def show(*args):
    print(args)
    total = 0
    for num in args:
        total += num
        
num = (1, 2, 3)
# show(num) #((1, 2, 3),) Invalido
show(*num)
