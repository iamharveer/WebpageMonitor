import getpass;
import smtplib;
import time;
import sys;
from Statics import *;

def FormatMIMEMsg(message, fromEmail, toEmail, subject):
    msg = MIMEText(message);
    msg['Subject'] = subject;
    msg['From'] = fromEmail;
    msg['To'] = toEmail;
    return msg;

def SendEmail(email, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587);
    server.ehlo();
    server.starttls();
    server.login(adminEmail, adminPassword);
    server.sendmail(adminEmail, email,  msg.as_string());

def GetAdminPassword():
    print("Please write sender's password for " + adminEmail);
    global adminPassword;
    adminPassword = getpass.getpass();
