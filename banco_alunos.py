# Importando sqlite3
import sqlite3

# Criando conexão com o banco de dados e o cursor
conn = sqlite3.connect("alunos_cadastrados.db")
cursor = conn.cursor()

# Criando tabela
with conn:
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   email TEXT,
                   telefone TEXT,
                   data_nascimento DATE,
                   idade INTEGER,
                   faixa TEXT
                   )''')