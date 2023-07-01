import sqlite3

caminho_banco_dados = r'f:\projeto_web\bd\usuario.db'

conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

opcao = input("Digite a opção desejada (1 - Excluir registros vazios, 2 - Excluir pelo ID): ")

class Manutencao:
    @staticmethod
    def del_vazio():
        cursor.execute("SELECT * FROM clientes WHERE nome IS NULL OR email IS NULL OR senha IS NULL")
        clientes_vazios = cursor.fetchall()
        for cliente in clientes_vazios:
            cursor.execute("DELETE FROM clientes WHERE id=?", (cliente[0],))

    @staticmethod
    def del_id():
        id_cliente = input("Digite o ID do cliente a ser excluído: ")
        cursor.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))

if opcao == '1':
    Manutencao.del_vazio()
    print("Registros vazios excluídos com sucesso!")
elif opcao == '2':
    Manutencao.del_id()
    print("Registro com ID especificado excluído com sucesso!")
else:
    print("Opção inválida!")

conexao.commit()
conexao.close()
