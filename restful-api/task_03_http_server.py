#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #ignore query string (ex: "/?id=...")
        # en ne prenant que le path (ex: "/")
        parsed = urlparse(self.path)
        path = parsed.path


        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode())

        elif path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting simple API server on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
