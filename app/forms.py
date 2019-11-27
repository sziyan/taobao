from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Enter password again', validators=[DataRequired()])

class OrderForm(FlaskForm):
    order_id = IntegerField("Order Number", validators=[DataRequired()])
    amount = DecimalField("Amount", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])