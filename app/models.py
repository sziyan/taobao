from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    orders = db.relationship('Orders', backref='buyer', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, unique=True, index=True, nullable=True)
    amount = db.Column(db.Float)
    ship_amount = db.Column(db.Float)
    status = db.Column(db.String(64))
    user_name = db.Column(db.Integer, db.ForeignKey('user.username'))

    def __repr__(self):
        return '<Orders {}>'.format(self.order_id)

