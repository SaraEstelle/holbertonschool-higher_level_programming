#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
"""Simple HTTP API using http.server with 404 handling."""


class MyHandler(BaseHTTPRequestHandler):
    """
    Handle GET requests and return
    text/JSON responses based on the requested path.
    """
    def do_GET(self):
        """
        Route GET requests based on self.path
        and send the appropriate response.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/data":
            self.send_response(200)
            data = {"name": "John", "age": 30, "city": "New York"}
            json_dict = json.dumps(data)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_dict.encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_dict = json.dumps(data)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_dict.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server = HTTPServer(("", 8000), MyHandler)
    server.serve_forever()
