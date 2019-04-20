from MySQLdb import connect

user = root
password = ''
db = 'me_estudos_son_python_com_db_api'
host = 'localhost'
port = 3306

connect(
    user=user,
    password=password, 
    db=db,
    host=host, 
    port=port
)

print('conectado!') 