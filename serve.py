import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
httpd = http.server.HTTPServer(('', 3000), http.server.SimpleHTTPRequestHandler)
print("Serving nexsun.ai at http://localhost:3000")
httpd.serve_forever()
