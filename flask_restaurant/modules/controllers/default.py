from flask import Flask, render_template, flash, redirect, url_for, request, send_file, make_response
from app import app
from modules.__init__ import db, login_manager
#from modules.models.forms import LoginForm, RegisterForm
#from modules.models.tables import User, CallLogs
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename


@app.route('/', methods=['GET'])
def index():
    return render_template('serving_template.html')


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()
    # return User.get_id(User.query.filter_by(id=id).first())


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Logado com sucesso!")
            if user.username == 'adm':
                return redirect(url_for("cadastro"))
            else:
                return redirect(url_for("index"))
        else:
            flash("Login inválido!")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Até mais!")
    return redirect(url_for("index"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        name = form.name.data
        email = form.email.data
        try:
            new_user = User(username, password, name, email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            flash('Ocorreu um erro, verifique os dados e tente novamente.')
    return render_template('cadastro.html', form=form)


@app.route("/home")
def home():
    return render_template("index.html")
