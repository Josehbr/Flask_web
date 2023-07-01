from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "77526D"


from app import  routes