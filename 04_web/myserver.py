from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse,unquote
import ssl
import logging
from datetime import datetime

#log config
logging.basicConfig(format='%(message)s',filename='access.log', encoding='utf-8', level=logging.DEBUG)

#change ip address
address = ('192.168.159.128', 443)

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'\r\nGET-----\r\n')
        self.analyze_request()

    def do_POST(self):
        logging.info(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'\r\nPOST-----\r\n')
        self.analyze_request()

    def do_PUT(self):
        logging.info(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'\r\nPUT-----\r\n')
        self.analyze_request()

    def do_DELETE(self):
        logging.info(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'\r\nDELETE-----\r\n')
        self.analyze_request()

    def analyze_request(self):
        # analyze request
        logging.info(unquote(self.path))
        logging.info(self.headers)
        
        content_length  = int(self.headers.get("content-length", 0))
        body = self.rfile.read(content_length).decode('utf-8')
        logging.info(unquote(body))
        
        # make response
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'200')

    
with HTTPServer(address, MyHTTPRequestHandler) as server:
    #if enable ssl 
    #creake certfile:openssl req -new -x509 -keyout .server.pem -out .server.pem -days 365 -nodes
    #if disable just comment out below line
    server.socket = ssl.wrap_socket(server.socket, certfile='/root/honeypot/wowhoneypot/server.pem', server_side=True)
    server.serve_forever()
