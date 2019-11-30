from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SubmitField, SelectField
from wtforms.validators import InputRequired,Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign In')

class OrderForm(FlaskForm):
    #order_id = IntegerField("Order Number", validators=[Optional()])
    amount = DecimalField("Amount(SGD)", validators=[InputRequired()])
    order_status = SelectField(u'Status', choices=[('paid', 'Paid'), ('pending', 'Pending')], validators=[InputRequired()])
    #ship_amount = DecimalField("Shipping Amount", validators=[Optional()])
    #ship_status = SelectField(u'Shipping Status', choices=[('paid', 'Paid'), ('not_paid', 'Not Paid')], default='pending', validators=[Optional()])
    #buyer = SelectField(u'Buyer', choices=[('yishan', 'Yi Shan'), ('yihui', 'Yi Hui'), ('sziyan', 'Zi Yan'), ('sooklau','Sook Lau'),('all','All')], validators=[InputRequired()])
    buyer = SelectField(u'Buyer', choices=[], validators=[InputRequired()])
    submit = SubmitField('Add Order')

class ShippingForm(FlaskForm):
    order_id = IntegerField("Order Number", validators=[Optional()])
    ship_amount = DecimalField("Shipping Amount(SGD)", validators=[Optional()])
    ship_status = SelectField(u'Shipping Status', choices=[('paid', 'Paid'), ('not_paid', 'Not Paid')], validators=[Optional()])
    submit = SubmitField('Add Shipment Info')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    name = StringField('Name', validators=[Optional()])
    password = PasswordField('Password', validators=[InputRequired()])
    password2 = PasswordField('Enter password again', validators=[InputRequired()])
    submit = SubmitField('Register')
