#NEC Forms Generator
import openpyxl
from openpyxl.styles import Alignment
import os
import datetime
from flask_mail import Mail, Message
from threading import Thread

from flask import Flask,render_template,redirect,url_for,flash,request


app = Flask(__name__)
SENDER = 'sziyanwao@gmail.com'
app.config['SENDER'] = SENDER

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
))

mail = Mail(app)
app.config['SENDER'] = 'sziyanwao@gmail.com'

project_dir = os.path.dirname(os.path.abspath(__file__))
template_file = os.path.join(project_dir,"template.xlsx")
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
month = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'October', 'November', 'December']
year = ['2019', '2020']
month_short = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject,sender,recipients,text_body,file_name):
   msg = Message(subject, sender=sender, recipients=recipients)
   msg.body = text_body
   with app.open_resource(file_name) as fp:
      msg.attach(file_name, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", fp.read())
   Thread(target=send_async_email, args=(app,msg)).start()

@app.route('/')
def home():
    return render_template("index.html",len = len(month), month=month, year=year)

@app.route("/update", methods=['POST','GET'])
def update():

    if request.form:
      my_file = openpyxl.load_workbook(template_file)
      sheet = my_file.get_sheet_by_name('Sheet1')
      month_selected = request.form.get('month')
      year_selected = request.form.get('year')
      for i in range(0,len(month)):
         if month_selected == month[i]:
            month_number = i
            sheet['B15'] =str((month_number + 1))
            sheet['D15'] = 'YEAR: ' + str(year_selected)
            sheet['B19'] = datetime.datetime(int(year_selected),int((month_number + 1)), 29)
            sheet['B51'] = '29 ' + '0'+str((month_number+1)) + ' ' + year_selected
            sheet['A13'] = 'Name: ' + request.form.get('name')
            cellB19 = sheet['B19']
            cellB19.alignment = Alignment(horizontal='right')
            file_name = 'Mobile Claim' + ' ' + str(month_short[month_number]) + ' ' + str(year_selected) +'.xlsx'
            month_short_str = str(month_short[month_number])
            my_file.save(file_name)
            recipient = request.form.get('email')
            subject_name = 'Mobile Claim for ' + month_short_str + ' ' + year_selected
            send_email(subject_name, sender=app.config['SENDER'], recipients=[recipient], text_body='Your monthly NEC mobile claim form.',file_name=file_name)
            os.remove(file_name)
            flash("Email sent successfully")
      flash("Report generated successfully")
    return redirect(url_for("home"))

if __name__ == "__main__":
 app.run(debug=True, host='192.168.1.68')