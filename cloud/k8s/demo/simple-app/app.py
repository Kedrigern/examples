from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pod_name = os.environ.get('MY_POD_NAME', 'unknown-pod')
        response = f"Hello from pod {pod_name}\n"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode())

if __name__ == '__main__':
    port = 8080
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()