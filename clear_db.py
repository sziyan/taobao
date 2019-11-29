from app import db
from app.models import User, Orders

users = User.query.all()
orders = Orders.query.all()

for u in users:
    db.session.delete(u)

for o in orders:
    db.session.delete(o)
db.session.commit()
print('Successfully cleared database!')