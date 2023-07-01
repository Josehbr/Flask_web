from app import app
from flask import render_template
from flask import request
import sqlite3


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():

    caminho_banco_dados = r'f:\projeto_web\bd\usuario.db'

    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    with sqlite3.connect(caminho_banco_dados) as conexao:
        cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE nome=? AND senha=?", (usuario, senha))
    resultado = cursor.fetchall()

    if resultado:
        return 'certo!'
    
    else:
        return 'erro'
    conexao.close()

