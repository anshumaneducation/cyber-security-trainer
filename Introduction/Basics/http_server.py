<<<<<<< HEAD
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
=======
# http_server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, this is the HTTP server!")

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
>>>>>>> 0bec01b071fca345744b304655bc863d895109b8
