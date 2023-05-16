import flask
from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

def send_email(message):

    sender = "flaskhomework@yandex.ru"
    password = "...."  # Хвала Яндексу, что не приходится светить реальным паролем

    server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    server.ehlo()

    try:

        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Text from site"
        server.sendmail(sender, sender, msg.as_string())
        return "The message was sent successfully!"

    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

@app.route('/')
def root():
    return render_template('main.html')

@app.route('/main.html#email_form')  # Переход по якорю
def link():
    return render_template("main.html#email_form")

@app.route('/submit', methods=['POST'])
def submit():
    email_text = request.form['text_to_send']
    send_email(message=email_text)
    return root()  # Это чтобы не уронить бэкенд


if __name__ == '__main__':
    app.run()




