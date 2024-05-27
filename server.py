import http.server
import socketserver

PORT = 8000  # Puedes cambiar el puerto si lo deseas

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()