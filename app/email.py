from threading import Thread
from flask import render_template
from flask_mail import Mail, Message
from app import mail
from ..flask_web import app

# 异步发送电子邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# 自动发邮件
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject, 
    sender=app.config['FLASK_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr