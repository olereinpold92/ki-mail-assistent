import http.server
import ssl
import os
import sys
import json
from datetime import datetime

PORT = 3000
CERT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certs')
CERT_FILE = os.path.join(CERT_DIR, 'localhost.crt')
KEY_FILE = os.path.join(CERT_DIR, 'localhost.key')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GEDAECHTNIS_DIR = os.path.join(BASE_DIR, 'gedaechtnis')

if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
    print("FEHLER: Zertifikate nicht gefunden in", CERT_DIR)
    print("Bitte zuerst generate-cert.bat ausfuehren")
    sys.exit(1)

os.chdir(BASE_DIR)

# Erlaubte Pfade fuer Schreibzugriff (nur innerhalb von gedaechtnis/)
ALLOWED_WRITE_PATHS = [
    'gedaechtnis/entries.json',
    'gedaechtnis/feedback/feedback_log.json',
    'gedaechtnis/feedback/analysis_log.json',
    'gedaechtnis/feedback/zusammenfassung.md',
    'gedaechtnis/feedback/chat_log.json',
    'gedaechtnis/regeln/ordner.json',
    'gedaechtnis/regeln/anhaenge.json',
    'gedaechtnis/kontakte/bekannte_absender.json',
]

class GedaechtnisHandler(http.server.SimpleHTTPRequestHandler):
    """Erweiterter Handler: Kann Dateien lesen UND in gedaechtnis/ schreiben."""

    def do_POST(self):
        # Nur /api/gedaechtnis erlaubt
        if not self.path.startswith('/api/gedaechtnis/'):
            self.send_error(404, 'Nicht gefunden')
            return

        # Datei-Pfad aus URL extrahieren (z.B. /api/gedaechtnis/feedback/chat_log.json)
        rel_path = self.path.replace('/api/gedaechtnis/', '')
        target = 'gedaechtnis/' + rel_path

        # Sicherheitscheck: Nur erlaubte Pfade
        if target not in ALLOWED_WRITE_PATHS:
            self.send_error(403, 'Schreibzugriff nicht erlaubt: ' + target)
            return

        # Body lesen
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        # Datei schreiben
        full_path = os.path.join(BASE_DIR, target)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        try:
            with open(full_path, 'wb') as f:
                f.write(body)
            print(f"[WRITE] {target} ({len(body)} Bytes)")
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'path': target}).encode())
        except Exception as e:
            self.send_error(500, str(e))

    def do_OPTIONS(self):
        """CORS Preflight-Anfragen beantworten."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        """CORS-Header bei jeder Antwort."""
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        """Weniger Spam im Terminal (nur POST-Requests loggen)."""
        if 'POST' in str(args) or 'ERROR' in str(args):
            super().log_message(format, *args)

httpd = http.server.HTTPServer(('localhost', PORT), GedaechtnisHandler)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(CERT_FILE, KEY_FILE)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

print("=" * 50)
print("KI Mail Assistent - HTTPS Server")
print("=" * 50)
print(f"Laeuft auf: https://localhost:{PORT}")
print(f"Taskpane:   https://localhost:{PORT}/addin/taskpane.html")
print(f"Gedaechtnis: {GEDAECHTNIS_DIR}")
print("")
print("Endpunkte:")
print(f"  GET  /gedaechtnis/...  → Dateien lesen")
print(f"  POST /api/gedaechtnis/... → Dateien schreiben")
print("")
print("Dieses Fenster NICHT schliessen!")
print("Zum Beenden: Strg+C oder Fenster schliessen")
print("=" * 50)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer gestoppt.")
    httpd.server_close()
