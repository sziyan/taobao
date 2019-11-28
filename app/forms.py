from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class OrderForm(FlaskForm):
    order_id = IntegerField("Order Number", validators=[DataRequired()])
    amount = DecimalField("Amount", validators=[DataRequired()])
    #status = StringField("Status", validators=[DataRequired()])
    status = SelectField(u'Status', choices=[('paid', 'Paid'), ('not_paid', 'Not Paid')], validators=[DataRequired()])
    submit = SubmitField('Add Order')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Enter password again', validators=[DataRequired()])
    submit = SubmitField('Register')
