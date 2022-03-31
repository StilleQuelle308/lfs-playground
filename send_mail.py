import smtplib
import ssl
from email.message import EmailMessage

from constants import MAIL_ACCOUNT
from constants import RECEIVER_EMAIL
from constants import SENDER_EMAIL

host = "smtp.ionos.de"
port = 465  # For SSL
tls = True
password = "Granatsplitter.Y0Y0"


def send_message_old(subject, body):
    context = ssl.create_default_context()

    message = "Subject: " + subject + "\n\n" + body

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(MAIL_ACCOUNT, password)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)


def send_message(subject, body):
    context = ssl.create_default_context()

    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(MAIL_ACCOUNT, password)
        server.send_message(message)