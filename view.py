# Importando o sqlite3
import sqlite3

# Criando conexão com o banco de dados
conn = sqlite3.connect("alunos_cadastrados.db")
cursor = conn.cursor()

# Operações de CRUD (create, read, update, delete) da aplicação

# Cadastrar/Inserir informações (create)
def create(lista):
    with conn:
        query = "INSERT INTO alunos (nome, email, telefone, data_nascimento, idade, faixa) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, lista)


# Mostrar/acessar informações (read)
def read():
    lista = []
    with conn:
        query = "SELECT * FROM alunos"
        cursor.execute(query)
        informacoes = cursor.fetchall()
        for informacao in informacoes:
            lista.append(informacao)
    return lista


# Atualizar informações (update)
def update(i):
    with conn:
        query = "UPDATE alunos SET nome = ?, email = ?, telefone = ?, data_nascimento = ?, idade = ?, faixa = ? WHERE id = ?"
        cursor.execute(query, i)


# Deletar informações (delete)
def delete(i):
    with conn:
        query = "DELETE FROM alunos WHERE id = ?"
        cursor.execute(query, i)
