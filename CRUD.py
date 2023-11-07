import mysql.connector

def mostrarDB(cursor):
    cursor.execute("SHOW DATABASES")
    print(f"Os Bancos de dados são: ", end='')
    for database in cursor:
        print(database[0], end='|')
    print()

def criarDB(cursor, dbname): 
    if not verificarSeDBExiste(cursor, dbname):
        cursor.execute(f"CREATE DATABASE {dbname}")
        print(f'O banco de dados {dbname} foi criado com exito')
    else:
        print(f"ERRO: Um banco de dados com o nome {dbname} já existe")

def verificarSeDBExiste(cursor, nome):
    nome = nome.lower()
    cursor.execute('SHOW DATABASES')
    for database in cursor:
        if database[0] == nome:
            return True
    return False

def deletarDB(cursor, dbname):
    if verificarSeDBExiste(cursor, dbname):
        cursor.execute(f'DROP DATABASE {dbname}')
        print(f'O banco de dados {dbname} foi deletado com exito')
    else:
        print(f'ERRO: Não foi encontrado um banco de dados com o nome de {dbname}!')

conexao = mysql.connector.connect(user='root', password='302302', host='127.0.0.1')
cursor = conexao.cursor(buffered=True)

mostrarDB(cursor)
criarDB(cursor, 'academia')
mostrarDB(cursor)
deletarDB(cursor, 'academia')
mostrarDB(cursor)

conexao.close()
