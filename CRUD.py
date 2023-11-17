import mysql.connector
import os

limpar_tela = lambda: os.system('cls')
conexao = mysql.connector.connect(user='root', password='302302', host='localhost', database='academia')
cursor = conexao.cursor()

#Retorna o id da entidade criada
def inserir_dados():
  valores = ['nome','CPF','telefone','endereco']
  for i in range(len(valores)):
    valores[i] = input(f'Digite um valor para a coluna {valores[i]}:')
  cursor.execute('INSERT INTO aluno (nome, CPF, telefone, endereco) VALUES (%s,%s,%s,%s)', tuple(valores))
  conexao.commit()
  print(f'O aluno com o ID {cursor.lastrowid} foi criado')

def mostrar_alunos():
  print('TABELA ALUNO')
  print(f'MATRICULA|{"NOME":<30}|{"CPF":<11}|{"TELEFONE":<11}|ENDEREÇO')
  cursor.execute('SELECT * FROM aluno')
  for (matricula, nome, CPF, telefone, endereco) in cursor:
    print(f'{matricula:<9}|{nome:<30}|{CPF:<11}|{telefone:<11}|{endereco}')

def puxar_dados(matricula_query):
  cursor.execute(f'SELECT * FROM aluno WHERE matricula = {matricula_query}')
  return cursor.fetchall()[0]

def atualizar_dados():
  matricula = int(input('Digite a matricula de um Aluno: '))
  aluno = puxar_dados(matricula)
  nome = input('Digite o novo nome do aluno: ') or aluno[1]
  CPF = input('Digite o novo CPF: ') or aluno[2]
  telefone = input('Digite o novo telefone: ') or aluno[3]
  endereco = input('Digite o novo endereço: ') or aluno[4]
  cursor.execute('UPDATE aluno SET nome = %s, CPF = %s, telefone = %s, endereco = %s WHERE matricula = %s',(nome, CPF, telefone, endereco, matricula))
  conexao.commit()

def deletar_dados(matricula):
  cursor.execute('DELETE FROM aluno WHERE matricula = %s', (matricula))
  conexao.commit()
  print(f'Aluno com matricula {matricula} deletado com exito.')

while True:
  menu = int(input(f'==========\n1 - Inserir Dados\n2 - Ler dados\n3 - Atualizar Dados\n4 - Deletar Dados\n5 - Sair\nSelecione uma opção: '))
  limpar_tela()
  match menu:
    case 1:
      inserir_dados()
    case 2:
      mostrar_alunos()
    case 3:
      mostrar_alunos()
      atualizar_dados()
    case 4:
      mostrar_alunos()
      deletar_dados(int(input('Digite a matricula do aluno: ')))
    case 5:
      break

conexao.close()
