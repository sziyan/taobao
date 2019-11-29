from app import app, db
from flask import render_template,redirect, url_for, flash
from app.forms import LoginForm, OrderForm, RegisterForm
from flask_login import current_user, login_user,login_required,logout_user
from app.models import User, Orders

@app.route("/")
@app.route("/index")
def index():
    orders = Orders.query.all()
    return render_template('index.html',orders=orders)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None and form.password.data == form.password2.data:
            new_user = User(username=form.username.data, name=form.name.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created! Kindly login now.")
            return redirect(url_for('login'))
        elif user is None and not form.password.data == form.password2.data:
            flash("Password does not match")
            return redirect(url_for('register'))
        flash("Username already exists")
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/add_order", methods=['GET', 'POST'])
@login_required
def add_order():
    form = OrderForm()
    if form.validate_on_submit():
        status = dict(form.status.choices).get(form.status.data)
        buyer = User.query.filter_by(username=form.buyer.data).first()
        if form.order_id.data is None: #submit empty order number
            order = Orders(amount=form.amount.data, status=status, buyer=buyer)
            db.session.add(order)
            db.session.commit()
            flash("Order added")
            return redirect(url_for('add_order'))
        exist_order = Orders.query.filter_by(order_id=form.order_id.data).first()  #search if order number exists in database
        if exist_order is None: #if does not exist in database
            order = Orders(order_id=form.order_id.data,amount=form.amount.data, status=status, buyer=buyer)
            db.session.add(order)
            db.session.commit()
            flash("Order added")
            return redirect(url_for('add_order'))
        flash("Order number exists in database.")
        return redirect(url_for('add_order'))
    return render_template('add_order.html', form=form)

@app.route("/orders")
@login_required
def orders():
    user = User.query.filter_by(username=current_user.username).first()
    buyer_orders = user.orders
    return render_template('orders.html',orders=buyer_orders)

