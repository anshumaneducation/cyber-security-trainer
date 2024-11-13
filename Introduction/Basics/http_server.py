from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the request handler
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # HTTP status code 200: OK
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World!")  # Write response

# Set up and start the server
server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("Server running on port 8080...")
httpd.serve_forever()
