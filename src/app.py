from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
import json 
from ast import literal_eval
# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

import requests
import formatos 


app = Flask(__name__)

csrf = CSRFProtect()#------------------------aqui csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)



@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Clave equivocada...sospechoso")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado :/")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    data = request.data
    print(data)
    return render_template('home.html')



@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


'''
formatos.door('1','True')
formatos.light('1','True')
formatos.light('2','False')
formatos.light('3','False')
formatos.buzz('1','False')'''



@app.route('/cambio', methods=['POST'])
def llegada():
    data = request.data
    objeto_json = literal_eval(data.decode('utf-8'))
    print("su bombillo es el:", objeto_json['id'], "y su estado es:", objeto_json['status'])
    return(objeto_json)









if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)

    app.run(host="0.0.0.0")






    