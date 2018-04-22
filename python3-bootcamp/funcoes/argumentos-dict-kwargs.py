def show(first, second, **kwargs):
    print(f'{first} and {second}')
    print('=========')
    print(kwargs)
        
nomes = {'first': 1, 'second': 2, 'jao': 'doido', 'pedrao': 'maluco'}
show(**nomes)
