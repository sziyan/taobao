from app import app, db
from flask import render_template,redirect, url_for, flash
from app.forms import LoginForm, OrderForm, RegisterForm, ShippingForm
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
    choice = []
    users = User.query.all()
    for u in users:
        label = u.name
        value = u.username
        choice.append((value,label))
    form.buyer.choices = choice
    if form.validate_on_submit():
        order_status = dict(form.order_status.choices).get(form.order_status.data)
        buyer = User.query.filter_by(username=form.buyer.data).first()
        order = Orders(amount=form.amount.data, order_status=order_status, buyer=buyer)
        db.session.add(order)
        db.session.commit()
        flash("Order added")
    return render_template('add_order.html', form=form)

@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    order = Orders.query.filter_by(id=id).first()
    form = ShippingForm()
    ship_status = dict(form.ship_status.choices).get(form.ship_status.data)
    if form.validate_on_submit():
        if form.order_id.data is not None:
            order.order_id = form.order_id.data
        if form.ship_amount.data is not None:
            order.ship_amount = form.ship_amount.data
        if form.ship_status.data is not None:
            order.ship_status = ship_status
        db.session.commit()
        flash("Shipping info updated")
    return render_template('edit.html', order=order, form=form)

@app.route("/orders")
@login_required
def orders():
    user = User.query.filter_by(username=current_user.username).first()
    buyer_orders = user.orders
    return render_template('orders.html',orders=buyer_orders)

@app.route("/reset")
@login_required
def reset():
    if not current_user.username == 'sziyan':
        return redirect(url_for('index'))
    entry1 = Orders.query.filter_by(id=2).first()
    db.session.delete(entry1)
    entry2 = Order.query.filter_by(id=2).first()
    db.session.delete(entry2)
    db.session.commt()
    return redirect(url_for('add_order'))

@app.route("/admin")
@login_required
def admin():
    if not current_user.isAdmin == 1:
        return redirect(url_for('index'))
    else:
        return render_template('admin.html')