from Statics import *;
import json;
import getpass;
import smtplib;
import time;
import sys;
from WebListener import *;
from Helpers import *;

def GetWebpageData(link):
    from urllib.request import urlopen;
    f = urlopen(link);
    return f.read();

def GetFileData(fp):
    f = open(fp, "rb");
    return f.read();

def SendText(phoneNumber):
    return;


def SendErrMsg(errMsg):
    msg = FormatMIMEMsg(errMsg, "harveersingh08@gmail.com", "harveersingh@live.com", "Error has occurred.");
    SendEmail("harveersingh@live.com", msg);

def GetUsersData(jsonFP):
    with open(jsonFP, "r") as read_file:
        return json.load(read_file);

def SendNotification():
    jsonData = GetUsersData(jsonFP);
    for user in jsonData:
        print("Sending notification to " + user["name"]);

        msg = FormatMIMEMsg(bodyMsg, adminEmail, user["email"], "PNP has been changed.");

        SendEmail(user["email"], msg);
        SendText(user["phoneNumber"]);

GetAdminPassword();
serverThread = WebListener("ServerThread", 8000, "localhost");
serverThread.start();

while(1):
    webpageData = "";
    fileData = "";

    try:
        webpageData = GetWebpageData(link);
        fileData = GetFileData(oldFP);
    except:
        SendErrMsg(u"Unexpected error:, '%s',\r\n error message: %s" %(sys.exc_info()[0], sys.exc_info()[1]));
        raise;

    if(   (webpageData != fileData)
       or True ):
        print("writing new data");

        try:
            SendNotification();
        except:
            SendErrMsg(u"Unexpected error:, '%s' \r\n error message: %s" %(sys.exc_info()[0], sys.exc_info()[1]));
            raise;

        with open(oldFP, "wb") as f:
            f.write(bytes(webpageData));
            f.close();

        time.sleep(interval);

serverThread.join();
