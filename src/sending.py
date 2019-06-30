import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import email

import os
from dotenv import load_dotenv
load_dotenv()

if not "emailPassword" in os.environ:
    raise ValueError("You should pass a email password")

gmail_user = os.environ["email"]
gmail_password = os.environ["emailPassword"]

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    print("Connected to gmail servers")
except:  
    print("Something went wrong...")

from_mail = gmail_user
to = input("Who should receive the mail?")
html = """  Buenos dias,

            A continuacion adjunto el informe generado sobre suicidios...

            Espero que os guste :)

            Javier Molins"""
msg = MIMEMultipart('alternative')
msg['Subject'] = "Pipelines Project Inform"
msg['From'] = gmail_user
msg['To'] = to
HTML_Contents = MIMEText(html, 'html')
filename = "../presentacion/Suicides Report.pdf"
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
fo.close()
attach.add_header('Content-Disposition','attachment',filename='Suicides Report')
msg.attach(attach)
msg.attach(HTML_Contents)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.close()