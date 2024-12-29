from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
import urllib.parse
import mimetypes
import os
import base64
import ssl
import json
import logging

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_parts = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(url_parts.query)

        file_path = '.' + self.path
        if os.path.exists(file_path):
            mime_type, _ = mimetypes.guess_type(file_path)
            self.send_response(200)
            self.send_header('Content-type', mime_type)
            self.end_headers()
            with open(file_path, 'rb') as file:
                self.wfile.write(file.read())
        else:
            auth_header = self.headers.get('Authorization')
            if auth_header:
                username, password = base64.b64decode(auth_header.split(' ')[1]).decode().split(':')
                if username == 'admin' and password == 'password':
                    message = f"Hello, {query.get('name', ['World'])[0]}!"
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes(message, "utf8"))
                else:
                    self.send_response(401)
                    self.end_headers()
                    self.wfile.write(b"Unauthorized")
            else:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b"Unauthorized")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        logging.info(f"Received POST request with body: {body}")

        auth_header = self.headers.get('Authorization')
        if auth_header:
            username, password = base64.b64decode(auth_header.split(' ')[1]).decode().split(':')
            if username == 'admin' and password == 'password':
                data = json.loads(body)
                logging.info(f"Received data: {data}")
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"POST request received successfully")
            else:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b"Unauthorized")
        else:
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b"Unauthorized")

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        logging.info(f"Received PUT request with body: {body}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"PUT request received successfully")

    def do_DELETE(self):
        logging.info("Received DELETE request")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"DELETE request received successfully")

    def send_error(self, code, message=None):
        logging.error(f"Error {code}: {message}")
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        error_page = f"<html><body><h1>{code} {message}</h1></body></html>"
        self.wfile.write(bytes(error_page, "utf8"))


def run_server():
    server_address = ('', 8000)
    httpd = ThreadingHTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='server.crt', keyfile='server.key', ssl_version=ssl.PROTOCOL_TLS)
    logging.info('Starting httpsd on port 8000...')
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()