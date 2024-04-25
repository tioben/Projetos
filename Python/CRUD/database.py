import os
import sqlite3 as lite

# Obtendo o caminho absoluto do arquivo database.py
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Criando o caminho absoluto para o arquivo studentsDatabase.db
caminho_db = os.path.join(diretorio_atual, "studentsDatabase.db")

# Criando conexão
conexão = lite.connect(caminho_db)

# Criando tabela
with conexão:
    cursor = conexão.cursor()
    cursor.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")

