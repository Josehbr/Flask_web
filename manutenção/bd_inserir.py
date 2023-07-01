import sqlite3

caminho_banco_dados = r'f:\projeto_web\bd\usuario.db'

id = int(input('id: '))
nome = input('nome: ')
email = input('email: ')
senha = input('senha: ')

with sqlite3.connect(caminho_banco_dados) as conexao:
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (id, nome, email, senha) VALUES (?, ?, ?, ?)", (id, nome, email, senha))
    conexao.commit()

conexao.close()
