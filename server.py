import http.server
import ssl
import os
import sys

PORT = 3000
CERT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certs')
CERT_FILE = os.path.join(CERT_DIR, 'localhost.crt')
KEY_FILE = os.path.join(CERT_DIR, 'localhost.key')

if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
    print("FEHLER: Zertifikate nicht gefunden in", CERT_DIR)
    print("Bitte zuerst generate-cert.bat ausfuehren")
    sys.exit(1)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('localhost', PORT), handler)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(CERT_FILE, KEY_FILE)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

print("=" * 50)
print("KI Mail Assistent - HTTPS Server")
print("=" * 50)
print(f"Laeuft auf: https://localhost:{PORT}")
print(f"Taskpane:   https://localhost:{PORT}/addin/taskpane.html")
print("")
print("Dieses Fenster NICHT schliessen!")
print("Zum Beenden: Strg+C oder Fenster schliessen")
print("=" * 50)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer gestoppt.")
    httpd.server_close()
