from flask import Flask, render_template, flash, redirect, url_for, request, send_file, make_response
from app import app
from modules.__init__ import db, login_manager
from modules.models.forms import LoginForm, RegisterForm, RegisterDish
from modules.models.tables import Waiter, Tables, Dish
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename
from modules.models.forms import RegisterDish, RegisterForm, LoginForm


@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')


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


@app.route("/cardapio")
def cardapio():
    dishes = Dish.getDishes()
    print(dishes)
    return render_template("cardapio.html", dishes=dishes)


@app.route("/cadastrar_prato", methods=['GET', 'POST'])
def cadastrar_prato():
    form = RegisterDish()

    # if form.validate_on_submit():
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        ingredients = form.ingredients.data
        image = form.image.data
        serves = form.serves.data
        if form.number_asked.data:
            number_asked = form.number_asked.data
        else:
            number_asked = 0

        filename = secure_filename(image.filename)

        try:
            new_dish = Dish(name, price, ingredients,
                            filename, serves, number_asked)
            db.session.add(new_dish)
            db.session.commit()
            image.save(os.path.join('modules/static/img/dishes', filename))
            return redirect(url_for('index'))
        except Exception as e:
            flash('Ocorreu um erro, verifique os dados e tente novamente: %s' % str(e))
    else:
        flash('Ocorreu um erro, verifique os dados e tente novamente.')
    return render_template("cadastrar_prato.html", form=form)


@app.route("/garcons")
def waiters():
    return render_template("index.html")


@app.route("/mesas")
def tables():
    return render_template("index.html")
