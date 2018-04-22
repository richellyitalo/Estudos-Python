def show(first, second):
    print(f'{first} and {second}')
        
nomes = {'first': 1, 'second': 2}
show(**nomes)
