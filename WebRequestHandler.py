import time;
from http.server import BaseHTTPRequestHandler, HTTPServer;
from Statics import *;
import json;
from Helpers import *;

def GetUsersData(jsonFP):
    with open(jsonFP, "r") as read_file:
        return json.load(read_file);

def WriteUsersData(data, jsonFP):
    with open(jsonFP, 'w') as outfile:
        json.dump(data, outfile);

def InsertNewEntry(name,email,phone):
    users = GetUsersData(jsonFP);
    for user in users:
        if(user["email"] == email):
            print("user entry already exists.");
            return False;

    jsonData = {}
    jsonData["name"] = name;
    jsonData["email"] = email;
    jsonData["phoneNumber"] = phone;
    users.append(jsonData);

    WriteUsersData(users, jsonFP);
    print("new user entry has been added: %s, %s, %s" %(name,email,phone));
    return True;

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200);
        self.send_header('Content-type', 'text/html');
        self.end_headers();

    def do_GET(self):
        if "formdata" in self.path:
            formData = self.path.split("?");
            userData = formData[1].split("&");
            name = (userData[0].split("="))[1];
            email = (userData[1].split("=")[1].split("%40"));
            emailAddress = email[0] + "@" + email[1];
            phone = userData[2].split("=")[1];

            if InsertNewEntry(name,emailAddress,phone):
                self.respond("Your user info has been added successfully, a welcome email will be sent to you.");
                msg = FormatMIMEMsg("You will be notified for any changes in PNP website", "harveersingh08@gmail.com", emailAddress, "Welcome!");
                SendEmail(emailAddress, msg);
            else:
                self.respond("User info already exists.");

        else:
            with open("Form.js", "r") as read_file:
                self.respond(read_file.read());

    def handle_http(self, status_code, content):
        self.send_response(status_code);
        self.send_header('Content-type', 'text/html');
        self.end_headers();
        return bytes(content, 'UTF-8');

    def respond(self, content):
        response = self.handle_http(200, content);
        self.wfile.write(response);
