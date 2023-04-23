import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()
password_env = os.getenv("PASSWORD")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "dothanhvinh1@gmail.com"
    password = password_env
    receiver = "dothanhvinh1@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)