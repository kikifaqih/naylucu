from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email , EqualTo


class loginadmin_F(FlaskForm):
    nama=StringField('nama', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(),Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

