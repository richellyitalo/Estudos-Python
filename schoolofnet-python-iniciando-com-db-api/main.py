from MySQLdb import connect

user = 'root'
password = ''
database = 'me_estudos_son_python_com_db_api'
host = 'localhost'
port = 3306

db = connect(
    user=user,
    password=password, 
    db=database,
    host=host, 
    port=port,
    autocommit=True
)

# db.commit()

# db.rollback()

# db.close()
cursor = db.cursor()

affected_rows = cursor.execute('SELECT * FROM bank_accounts')

print('affected_rows', affected_rows)

#print(list(cursor))

# maneiras de executar o loop entre os dados
# com fetchAll
# rows = cursor.fetchall()

# print('fetchall()')
# for row in rows:
#     print(row)

# # diretamente pelo cursor (utiliza o método mágico '__iter__(self):')
# print('__iter__ do cursor')
# for row in cursor:
#     print(row)

# fetchone() com fetchall()
# cursor.execute('SELECT * FROM bank_accounts')
# print(cursor.fetchone()) # 1 
# print(cursor.fetchall()) # restante após o 1
# print(cursor.fetchone()) # None
# print(cursor.fetchall()) # Tupla vazia

# fetchone no loop while
# cursor.execute('SELECT * FROM bank_accounts')
# row = cursor.fetchone()
# while row is not None:
#     print(row)

#     row = cursor.fetchone()

# fetchmany(LIMIT)
# cursor.execute('SELECT * FROM bank_accounts')
# rows = cursor.fetchmany(2)
# print(rows)
# rows = cursor.fetchmany(1)
# print(rows)
# rows = cursor.fetchmany(1)
# print(rows)

################################################
# INSERT DE DADOS
# cursor.execute("""
#     INSERT INTO bank_accounts (number, name, password, value, admin, agency_id) VALUES
#     ('1111-13', 'Mais um novo usuário', '123', 450.00, 0, 1)
#     """)

# cursor.execute('SELECT * FROM bank_accounts')
# print(list(cursor))


################################################
# UPDATE DE DADOS
# affected_rows = cursor.execute("""
#     UPDATE bank_accounts SET name = 'Fulaninho' WHERE number = '1111-12'
#     """)
# print('affected_rows', affected_rows)
# print('rowcount', cursor.rowcount)

################################################
# UPDATE DE DADOS
# affected_rows = cursor.execute("""DELETE FROM bank_accounts WHERE number = '1111-12'""")
# print(affected_rows)
# print(cursor.rowcount)


# Queries passando parametros
# name = 'Fulano de tal etc'
# number = '0001-01'
# value = 150_350
# cursor.execute("UPDATE bank_accounts SET name = %s, value = %s WHERE number = %s",
#     (name, value, number)
# )


# EXECUTANDO MULTIPLAS QUERIES
# E commits
db.autocommit(False)

try:
    affected_rows = cursor.executemany(
        """
        INSERT INTO bank_accounts (number, name, password, value, admin, agency_id) VALUES
        (%s, %s, %s, %s, %s, %s)
        """,
        (
            ('9999-13', 'Mais um novo usuário', '123', 450.00, 0, 1),
            ('9999-14', 'Mais um novo usuário', '123', 450.00, 0, 1),
            ('9999-15', 'Mais um novo usuário', '123', 450.00, 0, 1)
        )
    )
    cursor.execute("""
        INSERT INTO bank_accounts (number, name, password, value, admin, agency_id) VALUES
        (%s, %s, %s, %s, %s, %s)
        """,
        ('9999-13', 'Mais um novo usuário', '123', 450.00, 0, 1)
    )

    db.commit()
    
    print('registros realizados', affected_rows)
except:
    db.rollback()
    print('Não foi possível rodar a consulta')
else:
    print('Foi possível rodar a consulta')
finally:
    print('Aqui no finally tudo é possível')

cursor.execute('SELECT * FROM bank_accounts')
print(tuple(cursor))

db.close()