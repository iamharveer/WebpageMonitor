import time;
import threading;
from http.server import BaseHTTPRequestHandler, HTTPServer;
from WebRequestHandler import WebRequestHandler;

class WebListener (threading.Thread):
    def __init__(self, threadName, port, hostname):
        threading.Thread.__init__(self);
        self.name = threadName;
        self.portNumber = port;
        self.hostname = hostname;

    def run(self):
        print("running server now.");
        self.StartWebListener();

    def StartWebListener(self):
        print ("Started listening on port: %s" %(self.portNumber));
        server_class = HTTPServer;
        httpd = server_class((self.hostname, self.portNumber), WebRequestHandler);

        try:
            httpd.serve_forever();
        except KeyboardInterrupt:
            raise;

        httpd.server_close();
