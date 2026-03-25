# KI Mail Assistent – Projektstand (25.03.2026)

## Kontext & Person
- Ole Reinpold, Du-Ansprache, Deutsch, kein Techniker
- Prokurist/GF: Elbe Hernien Centrum EHC GmbH (kurz: EHC)
- Mitgruender/GF: Qodia GmbH
- E-Mail: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- Arbeitsstil: Ole macht einfache Klicks selbst, Claude uebernimmt komplexe Konfigurationen und Code. Keine Fachjargon-Erklaerungen.

## Tech Stack
- HTML + CSS + Vanilla JS (keine Frameworks), alles in einer index.html
- GitHub: olereinpold92/ki-mail-assistent (Token in 1Password, kein Ablauf)
- Netlify: https://bright-cannoli-eeaa45.netlify.app / Login: EHC2026
- Auto-Deploy ist AKTIV (wurde heute aktiviert fuer Push)
- Netlify Build-Credits: fast aufgebraucht fuer Maerz – sparsam deployen!
- Azure Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Azure Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Azure Redirect URI: https://bright-cannoli-eeaa45.netlify.app/
- Azure Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite + Adminzustimmung erteilt

## Deploy-Workflow (WICHTIG)
- Code wird als EINE index.html gepusht (kein separates app.js)
- Push via GitHub API mit Token aus 1Password
- SHA der aktuellen index.html immer frisch per API holen
- Vor jedem Deploy: Preview lokal zeigen, erst nach Freigabe durch Ole pushen
- NIEMALS outerHTML des Browsers pushen - immer die RAW Datei vom Server (/home/claude/preview6.html)

## Aktueller Live-Stand
- URL: https://bright-cannoli-eeaa45.netlify.app (Login: EHC2026)
- Aktiver Deploy: main@50032d0 (vom 24.03.2026, 21:21 Uhr) - alter Stand ohne neues UI!
- PROBLEM: preview6.html wurde nicht korrekt deployed, Seite war kurz kaputt, wurde zurueckgesetzt

## Was in preview6.html fertig ist (auf dem Server: /home/claude/preview6.html)
DIESES FILE MUSS NOCH KORREKT DEPLOYED WERDEN!

### UI Features:
1. 4-Spalten-Layout: Ordner-Sidebar | Mail-Liste | Mail-Inhalt | KI-Panel
2. Verschiebbare Spaltenbreiten (Drag-to-resize), Einstellung wird gespeichert
3. Alle Spalten auf/zuklappbar, Einstellung wird gespeichert
4. Prio manuell anpassbar (5 Buttons: Wichtig & Dringend / Wichtig / Muss / Nice to have / Nachhalten)
5. KI-Analyse einklappbar (standardmaessig zu)
6. Aufgabenliste: KI schlaegt Aufgaben vor (max 3, keine Teilschritte, keine Ablage-Aufgaben), Ole kann ergaenzen/abharken/loeschen
7. Ablegen-Bereich: Mail verschieben + jeder Anhang mit eigenem editierbaren Dateinamen (JJMMTT_Org_Name.ext) + Ordner-Selector + "Neuer Unterordner"-Funktion
8. Antwort als Toggle (Ja/Nein) - bei Nein trotzdem KI-Antwort generierbar
9. Feedback: "Alles 100% korrekt" / "Nicht korrekt" + Freitextfeld
10. Wiederkehrende Mails: Toggle + Intervall, KI merkt sich Einstellungen
11. "Alles bestaetigen & ausfuehren": Ein Klick -> Mail verschieben + Anhaenge ablegen + Antwort senden + KI lernt

### Technische Features (echte Graph API):
12. Echte Outlook-Ordner laden (inkl. Ungelesen-Zaehler, Unterordner)
13. Klick auf Ordner laedt Mails aus diesem Ordner
14. Mail wirklich verschieben via Graph API
15. OneDrive-Ordner laden (echte Ordnerstruktur im Dropdown)
16. Anhang in OneDrive ablegen (echte Upload-Funktion)
17. KI lernt aus Anpassungen (Prio, Ordner, Antwort) UND aus Feedback

### KI-Prompt-Regeln (entschieden):
- Aufgaben: Nur was UEBER Antworten+Ablegen hinausgeht, keine Teilschritte, keine Ablage-Aufgaben, max 3
- keine_antwort_noetig: true bei Rechnungen, Newslettern, Infomails
- KI lernt aus Korrekturen via localStorage

## Naechste Aufgabe (PRIORITAET 1)
preview6.html korrekt als index.html ins GitHub pushen und deployen.

So geht es richtig:
1. SHA der aktuellen index.html per API holen
2. Den Inhalt von /home/claude/preview6.html per Python base64-kodieren
3. Via GitHub API PUT pushen mit korrektem SHA
4. Netlify deployed automatisch (Auto-Deploy ist aktiv)

FEHLER den ich heute gemacht habe: Ich habe document.documentElement.outerHTML base64-kodiert statt die raw Datei. Das hat eine kaputte HTML-Datei erzeugt.

## OneDrive Ordnerstruktur
EHC: Eingangsrechnungen, Vertraege, Korrespondenz, Personal, Finanzen, OP-Dokumentation
Qodia: Allgemein, Investoren, Vertraege
Privat: Allgemein
Kein Anhang

## Prioritaetssystem
Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten

## Dateiformat fuer Anhaenge
JJMMTT_Organisation_Dateiname.ext (z.B. 260324_Helios_Kliniken_Rechnung_2026-0342.pdf)
