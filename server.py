from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

port = 8000
print(f"Starting server at http://localhost:{port}")
print("Drücken Sie STRG+C zum Beenden")
HTTPServer(('localhost', port), CORSRequestHandler).serve_forever() 