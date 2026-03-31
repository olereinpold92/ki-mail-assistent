import http.server
import ssl
import os
import sys
import json
import socket
from datetime import datetime

PORT = 3000
CERT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certs')
CERT_FILE = os.path.join(CERT_DIR, 'localhost.crt')
KEY_FILE = os.path.join(CERT_DIR, 'localhost.key')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Shared-Verzeichnis: Liest Pfad aus shared-path.config (fuer geteiltes Gedaechtnis)
# Fallback: BASE_DIR (altes Verhalten, falls Config nicht existiert)
SHARED_CONFIG = os.path.join(BASE_DIR, 'shared-path.config')
if os.path.exists(SHARED_CONFIG):
    with open(SHARED_CONFIG, 'r', encoding='utf-8') as f:
        SHARED_DIR = f.read().strip()
    if not os.path.isdir(SHARED_DIR):
        print(f"WARNUNG: Shared-Pfad existiert nicht: {SHARED_DIR}")
        print(f"Fallback auf lokales Verzeichnis: {BASE_DIR}")
        SHARED_DIR = BASE_DIR
else:
    SHARED_DIR = BASE_DIR

GEDAECHTNIS_DIR = os.path.join(SHARED_DIR, 'gedaechtnis')

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

    def translate_path(self, path):
        """Leitet /gedaechtnis/-Anfragen auf SHARED_DIR um."""
        # Nur /gedaechtnis/ umleiten, alles andere normal servieren
        if path.startswith('/gedaechtnis/') or path == '/gedaechtnis':
            # Pfad relativ zu SHARED_DIR aufloesen
            rel = path[1:]  # Fuehrenden / entfernen
            return os.path.join(SHARED_DIR, rel.replace('/', os.sep))
        return super().translate_path(path)

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

        # Datei schreiben (in SHARED_DIR, nicht BASE_DIR)
        full_path = os.path.join(SHARED_DIR, target)
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
        """CORS-Header + No-Cache bei jeder Antwort (verhindert Caching im Desktop-Outlook)."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        """Weniger Spam im Terminal (nur POST-Requests loggen)."""
        if 'POST' in str(args) or 'ERROR' in str(args):
            super().log_message(format, *args)

# Dual-Stack Server: empfaengt sowohl IPv4 (127.0.0.1) als auch IPv6 (::1)
# Noetig weil OAuth-Popup-Fenster 'localhost' manchmal als ::1 aufloesung
class DualStackServer(http.server.HTTPServer):
    def server_bind(self):
        if hasattr(socket, 'AF_INET6') and hasattr(socket, 'IPV6_V6ONLY'):
            try:
                self.socket.close()
                self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            except Exception:
                pass  # Fallback: normaler IPv4-Socket
        super().server_bind()

try:
    httpd = DualStackServer(('::', PORT), GedaechtnisHandler)
except OSError:
    # Fallback falls :: nicht verfuegbar
    httpd = http.server.HTTPServer(('0.0.0.0', PORT), GedaechtnisHandler)

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
