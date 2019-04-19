import os

print('caminho absoluto até a pasta atual do arquivo')
print(os.path.abspath('.'))

print(os.path.abspath('./pac/subpac1/pac2.py'))

path_file = os.path.abspath('./pac/subpac1/pac2.py')
print(os.path.dirname(path_file))

print('*** concatenando caminho')
path_file_joined = os.path.join(os.path.abspath('.'), 'pac', 'subpac1', '__init__.py')
print(os.path.exists(path_file_joined))
print(path_file_joined)
