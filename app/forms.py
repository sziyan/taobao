from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SubmitField, SelectField
from wtforms.validators import InputRequired,Optional


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign In')

class OrderForm(FlaskForm):
    order_id = IntegerField("Order Number", validators=[Optional()])
    amount = DecimalField("Amount", validators=[InputRequired()])
    buyer = SelectField(u'Buyer', choices=[('yishan', 'Yi Shan'), ('yihui', 'Yi Hui'), ('sziyan', 'Zi Yan'), ('sooklau','Sook Lau'),'all','All'], validators=[InputRequired()])
    status = SelectField(u'Status', choices=[('paid', 'Paid'), ('pending', 'Pending')], validators=[InputRequired()])
    submit = SubmitField('Add Order')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    name = StringField('Name', validators=[Optional()])
    password = PasswordField('Password', validators=[InputRequired()])
    password2 = PasswordField('Enter password again', validators=[InputRequired()])
    submit = SubmitField('Register')
