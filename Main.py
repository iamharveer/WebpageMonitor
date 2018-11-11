from Statics import *;
import json;
import getpass;
import smtplib;
import time;
import sys;

def GetWebpageData(link):
    from urllib.request import urlopen;
    f = urlopen(link);
    return f.read();

def GetFileData(fp):
    f = open(fp, "rb");
    return f.read();

def SendText(phoneNumber):
    return;

def SendEmail(email, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587);
    server.ehlo();
    server.starttls();
    server.login(adminEmail, adminPassword);

    print(msg);

    server.sendmail(adminEmail, email,  msg.as_string());

def SendErrMsg(errMsg):
    msg = MIMEText(errMsg,"html");
    FormatMIMEMsg(msg, "harveersingh08@gmail.com", "harveersingh@live.com", "Error has occurred.");
    SendEmail("harveersingh@live.com", msg);

def GetUsersData(jsonFP):
    with open(jsonFP, "r") as read_file:
        return json.load(read_file);

def FormatMIMEMsg(msg, fromEmail, toEmail, subject):
    msg = bodyMsg;
    msg['Subject'] = subject;
    msg['From'] = fromEmail;
    msg['To'] = toEmail;
    return msg;

def SendNotification():
    jsonData = GetUsersData(jsonFP);
    for user in jsonData:
        print("Sending notification to " + user["name"]);

        SendEmail(user["email"], FormatMIMEMsg(bodyMsg, adminEmail, user["email"], "PNP has been changed."));
        SendText(user["phoneNumber"]);

print("Please write sender's password for " + adminEmail);
adminPassword = getpass.getpass();

while(1):
    webpageData = "";
    fileData = "";

    try:
        webpageData = GetWebpageData(link);
        fileData = GetFileData(oldFP);
    except:
        SendErrMsg("Unexpected error:, '%s'" %(sys.exc_info()[0]));
        raise;

    if(   (webpageData != fileData)
       or 1 ):
        print("writing new data");

        try:
            SendNotification();
        except:
            SendErrMsg("Unexpected error:, '%s' \r\n %s" %(sys.exc_info()[0], sys.exc_info()[1]));
            raise;

        with open(oldFP, "wb") as f:
            f.write(bytes(webpageData));
            f.close();

        time.sleep(60*5);
