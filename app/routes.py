from app import app
from flask import render_template, request, flash, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

caminho_banco_dados = r'f:\projeto_web\bd\usuario.db'
engine = create_engine(f'sqlite:///{caminho_banco_dados}')
session = Session(bind=engine)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
    


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    cliente = session.query(Cliente).filter_by(nome=usuario, senha=senha).first()

    if cliente:
        email = cliente.email
        return render_template('autenticar.html', usuario=usuario, email=email)
    else:
        flash("dados incorretos")
        return redirect ('/login')

