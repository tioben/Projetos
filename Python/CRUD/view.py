import os
import sqlite3 as lite

# Obtendo o caminho absoluto do arquivo view.py
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Criando o caminho absoluto para o arquivo studentsDatabase.db
caminho_db = os.path.join(diretorio_atual, "studentsDatabase.db")

# Criando conexão
conexão = lite.connect(caminho_db)

#C-R-U-D 
#C = Creaty
#R = Ready
#U = Update
#D = Delete

# Inserir dados CREATY
def creaty(i):
    with conexão:
        cursor = conexão.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, i) 
  
# Acessar dados READY
def ready ():
    RegistrationList = [] 
    with conexão:
        cursor = conexão.cursor()
        query = "SELECT * FROM formulario"
        cursor.execute(query)
        register = cursor.fetchall()
        for i in register:
            RegistrationList.append(i)
        return RegistrationList

# Atualizar dados UPDATE
def update_info(userInfoParameter):
    with conexão:
        cursor = conexão.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cursor.execute(query, userInfoParameter)

# Deletar dados DELETE
def delete_info(i):
    with conexão:
        cursor = conexão.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cursor.execute(query,i)
    