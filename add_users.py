from app import db
from app.models import User

#Initialize users

#yishan
yishan = User(username="yishan", name="Yi Shan")
yishan.set_password('P@ssw0rd')
db.session.add(yishan)

#yihui
yihui = User(username="yihui", name="Yi Hui")
yihui.set_password('P@ssw0rd')
db.session.add(yihui)

#sooklau
sooklau = User(username="sooklau", name="Sook Lau")
sooklau.set_password('P@ssw0rd')
db.session.add(sooklau)

#all
all = User(username="all", name="All")
all.set_password('P@ssw0rd')
db.session.add(all)

#add to database
db.session.commit()

#Output message
print("Users created")