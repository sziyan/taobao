from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SubmitField, SelectField
from wtforms.validators import InputRequired,Optional
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login_submit = SubmitField('Sign In')

class OrderForm(FlaskForm):
    amount = DecimalField("Amount(SGD)", validators=[Optional()])
    order_status = SelectField(u'Status', choices=[('paid', 'Paid'), ('pending', 'Pending')], validators=[Optional()])
    buyer = SelectField(u'Buyer', choices=[], validators=[Optional()])
    order_submit = SubmitField('Add Order')

    def update_choices(self):
        new_choice = []
        all_users = User.query.all()
        for u in all_users:
            label = u.name
            value = u.username
            new_choice.append((value, label))
        self.buyer.choices = new_choice

class ShippingForm(FlaskForm):
    order_id = IntegerField("Order Number", validators=[Optional()])
    ship_amount = DecimalField("Shipping Amount(SGD)", validators=[Optional()])
    ship_status = SelectField(u'Shipping Status', choices=[('paid', 'Paid'), ('not_paid', 'Not Paid')], validators=[Optional()])
    shipping_submit = SubmitField('Add Shipment Info')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Optional()])
    name = StringField('Name', validators=[Optional()])
    password = PasswordField('Password', validators=[InputRequired()])
    password2 = PasswordField('Enter password again', validators=[InputRequired()])
    register_submit = SubmitField('Register')

class EditUserForm(FlaskForm):
    username = SelectField(u'Username', choices=[], validators=[InputRequired()])
    name = StringField('Name', validators=[Optional()])
    password = PasswordField('Password', validators=[Optional()])
    password2 = PasswordField('Enter password again', validators=[Optional()])
    edit_submit = SubmitField('Update')

    def update_choices(self):
        new_choice = []
        all_users = User.query.all()
        for u in all_users:
            label = u.name
            value = u.username
            new_choice.append((value, label))
        self.username.choices = new_choice

class DeleteUserForm(FlaskForm):
    username = SelectField(u'Username', choices=[], validators=[InputRequired()])
    delete_submit = SubmitField('Delete User')

    def update_choices(self):
        new_choice = []
        all_users = User.query.all()
        for u in all_users:
            label = u.name
            value = u.username
            new_choice.append((value, label))
        self.username.choices = new_choice

class AddUser(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    name = StringField('Name', validators=[Optional()])
    add_user_submit = SubmitField('Add User')

class DeleteOrderForm(FlaskForm):
    delete_order_submit = SubmitField("Delete this order")