from flask_wtf.file import FileField, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterDish(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    ingredients = StringField('ingredients', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired()])
    serves = IntegerField('serves', validators=[DataRequired()])
    number_asked = IntegerField('number_asked')
