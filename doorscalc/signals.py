from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail, EmailMessage
import smtplib

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


@receiver(post_save, sender=Order)
def order_notification(sender, instance, created, **kwargs):
    print("New Order placed!\n--------------")
    u = instance.user
    print("%s has already ordered new doors" % u )
    send_mail("mateusz.ignatowicz@icloud.com", "Thanks for ordering doors", "Dear "+str(u)+"\nThank You for ordering. We have already placed it" )
    print('something happened')

    