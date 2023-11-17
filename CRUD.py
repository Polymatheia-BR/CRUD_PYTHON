import mysql.connector

conexao = mysql.connector.connect(user='root', password='302302', host='localhost', database='academiaturmac')
cursor = conexao.cursor()

def inserir_dados(query, valores):
  for i in range(len(valores)):
    valores[i] = input(f'Digite um valor para a coluna {valores[i]}:')
  cursor.execute(query, tuple(valores))
  conexao.commit()
  print(f'A entidade com o ID {cursor.lastrowid} foi criada')

def mostrar_dados(tabela):
    cursor.execute(f"SELECT * FROM {tabela}")
    print(f'TABELA {tabela.upper()}')
    colunas = cursor.column_names
    for x in range(len(colunas)):
        print(colunas[x].capitalize() + ' | ', end='')
    print()

    dados = cursor.fetchall()
    for linha in dados:
        print(' | '.join([str(i) for i in linha]))
    input()

def deletar_dados(query):
    id = int(input('Digite a chave primaria da entidade que deseja deletar: '))
    cursor.execute(query, id)
    conexao.commit()
    print(f'Entidade com o id {id} deletado!')

while True:
    tabela = int(input('==========\n1 - Aluno\n2 - Funcionario\n3 - Matriculado\n4 - Modalidade\nSelecione uma tabela:'))
    match tabela:
        case 1:
            tabela = 'aluno'
            query_insert = 'INSERT INTO aluno (nome, CPF, telefone, endereco) VALUES (%s,%s,%s,%s)'
            query_delete = 'DELETE FROM aluno WHERE matricula = %s'
            valores = ['nome', 'CPF', 'telefone', 'endereco']
        case 2:
            tabela = 'funcionario'
            query_insert = 'INSERT INTO funcionario (nome, CPF, departamento, salario, email) VALUES (%s,%s,%s,%s,%s)'
            query_delete = 'DELETE FROM funcionario WHERE id_funcionario = %s'
            valores = ['nome', 'CPF', 'departamento', 'salario', 'email']
        case 3:
            tabela = 'matriculado'
            query_insert = 'INSERT INTO matriculado (fk_matricula) VALUES (%s)'
            query_delete = 'DELETE FROM matriculado WHERE id_matriculado = %s'
            valores = ['fk_matricula']
        case 4:
            tabela = 'modalidade'
            query_insert = 'INSERT INTO modalidade (nome, duracao) VALUES (%s,%s)'
            query_delete = 'DELETE FROM modalidade WHERE ID = %s'
            valores = ['nome','duracao']
        case _:
            print("Digite uma tabela valida!")

    menu = int(input(f'==========\n1 - Inserir Dados\n2 - Ler dados\n3 - Deletar Dados\n4 - Sair\nSelecione uma opção: '))
    match menu:
        case 1:
            inserir_dados(query_insert, valores)
        case 2:
            mostrar_dados(tabela)
        case 3:
            mostrar_dados(tabela)
            deletar_dados(query_delete)
        case _:
            print('Opção invalida!')
