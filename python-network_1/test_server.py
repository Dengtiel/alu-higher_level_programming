from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Log incoming request for debugging purposes
        print(f"Received request for: {self.path}")
        
        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"It works!")  # Response body for /status endpoint
        else:
            super().do_GET()  # Let SimpleHTTPRequestHandler handle other paths

if __name__ == "__main__":
    server_address = ('0.0.0.0', 5050)  # Bind to all IP addresses on port 5050
    try:
        httpd = HTTPServer(server_address, MyHandler)
        print("Server running at http://0.0.0.0:5050/")
        httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}")
        print("Port might already be in use. Try using a different port.")
