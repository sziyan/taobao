from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    orders = db.relationship('Orders', backref='buyer', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, unique=True, index=True)
    amount = db.Column(db.Float)
    user_name = db.Column(db.Integer, db.ForeignKey('user.username'))

    def __repr__(self):
        return '<Orders {}>'.format(self.order_id)