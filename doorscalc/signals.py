from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail, EmailMessage
import smtplib

def email():    
    email = EmailMessage('Subject', 'Body', to=['contact@mign.pl'])
    email.send()
    print('something happened')

def send_mail(target, topic, msg):
    subject = topic
    description =  msg
    gmail_user =  "mp.ignatowicz@gmail.com" # email id from where you want send mail
    gmail_pwd ="lubiete1231886"
    FROM = 'Admin: <from@gmail.com>'
    TO = target #email id where you want send mail
    TEXT = description
    SUBJECT = subject
    server = smtplib.SMTP_SSL()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, TO, SUBJECT, TEXT)

    server.sendmail(FROM, TO, message)
    server.quit() 
    print('end..............')   




    