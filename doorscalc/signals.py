from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail, EmailMessage
import smtplib

def email():    
    email = EmailMessage('Subject', 'Body', to=[''])
    email.send()
    print('something happened')

def send_mail(target, topic, msg):
    subject = topic
    description =  msg
    gmail_user =  "" # email id from where you want send mail
    gmail_pwd =""
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


@receiver(post_save, sender=Order)
def order_notification(sender, instance, created, **kwargs):
    print("New Order placed!\n--------------")
    u = instance.user
    emailu = instance.user.email
    w = instance.w
    h = instance.h
    d = instance.d
    customer = instance.customer
    measure = ''

    if d is None or d == "None":
        measure = ('%sx%s' % (w,h))
    else: 
        measure = ('%sx%sx%s' % (w,h,d))
    if created:
        print("%s ORDERED NEW DOORS" % u )
        print("Measure: %s" % measure)
        email = EmailMessage('%s has already placed an order!' % u, 'Measure: '+measure+'\nFinal customer: '+customer+'\n\n', to=['contact@mign.pl'])
        email.send()
    else:
        print('Nobaby knows what')

    