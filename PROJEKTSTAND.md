# KI Mail Assistent – Projektstand (25.03.2026)

## Wichtig: Kein Gedaechtnis zwischen Chats
Claude hat kein Gedaechtnis. Jeden neuen Chat mit diesem Satz starten:
"Lies https://raw.githubusercontent.com/olereinpold92/ki-mail-assistent/main/PROJEKTSTAND.md und mach weiter."
Alle Entscheidungen hier dokumentieren damit sie nicht nochmal diskutiert werden muessen.

## Wer ist Ole?
- Ole Reinpold, Ansprache: Du, Sprache: Deutsch
- Prokurist/GF: Elbe Hernien Centrum EHC GmbH (Hamburger Hernien Centrum), 2 Standorte Hamburg, ~8 Mitarbeiter, Hernienchirurgie
- Mitgruender/GF: Qodia GmbH (KI-Loesungen GOAe-Abrechnung), 4 Gruender
- E-Mail: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- Kein Entwickler, Technikaffinitaet 6-7/10. Claude uebernimmt komplexen Code, Ole macht einfache Klicks selbst.
- Ole will direkte Anleitungen, nicht durch UI navigiert werden. Lieber Ole anleiten als selbst navigieren.
- Ole will als Sparringspartner gefordert werden, nicht nur bestaetigt.

## Warum dieser KI Mail Assistent?
Ole bearbeitet taeglich viele E-Mails als GF von EHC und Qodia. Das kostet zu viel Zeit.
Ziel: Jeden Morgen Interface oeffnen, alle neuen Mails sehen, KI-Analyse lesen, mit einem Klick abarbeiten.
Langfristig: KI handelt autonom in Oles Sinne. Kurzfristig: KI macht Vorschlaege, Ole bestaetigt.

## Was der Assistent koennen soll (pro Mail)
1. Prioritaet vorschlagen: Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten
2. Antwortvorschlag generieren (in Oles Stil, auf Deutsch, bearbeitbar)
3. E-Mail-Ordner vorschlagen (wo die Mail in Outlook abgelegt werden soll)
4. Anhaenge in OneDrive ablegen mit Dateiname: JJMMTT_Organisation_Dateiname.ext
5. Weiterfuehrende Aktionen benennen (z.B. Rechnung bezahlen, Daten einpflegen)
6. Feedback-System: Ole gibt Sterne + Text, KI lernt daraus

## Tech Stack
- Alles in einer index.html + app.js (keine Frameworks)
- GitHub Repo: olereinpold92/ki-mail-assistent
- Netlify: https://bright-cannoli-eeaa45.netlify.app / Login: EHC2026
- Auto-Deploy: aktiv (Push auf main triggert Netlify)
- Netlify Build-Credits: fast aufgebraucht fuer Maerz - sparsam deployen!
- Azure Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Azure Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Azure Redirect URI: https://bright-cannoli-eeaa45.netlify.app/
- Azure Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite + Adminzustimmung erteilt

## Deploy-Workflow (EINZIGER funktionierender Weg)
1. Claude erstellt index.html und stellt sie als Download bereit (present_files Tool)
2. Ole laedt die Datei herunter
3. github.com/olereinpold92/ki-mail-assistent -> "Add file" -> "Upload files"
4. Datei als index.html hochladen -> Commit changes
5. Netlify deployed automatisch (1-2 Min warten)

NIEMALS versuchen:
- outerHTML pushen (erzeugt kaputte Datei)
- Datei in Chunks via JavaScript uebertragen (10KB Limit, Datei ist 75KB)
- Datei-Dialog automatisch oeffnen (Browser-Sicherheitssperre)
- GitHub API via Browser-JS fuer grosse Dateien (10KB Limit)

## Entschiedene Punkte - NICHT nochmal diskutieren
- Claude Code: ABGELEHNT. Ole ist kein Entwickler, zu viel Einrichtungsaufwand.
- n8n/Make.com/Power Automate: VERWORFEN. Direkte Graph API im Interface ist besser.
- Ein-Datei-Ansatz (index.html + app.js): BEIBEHALTEN
- App-Passwort: EHC2026
- Hoster: Netlify (GitHub Pages deaktiviert)
- Microsoft 365 als Mail-Hub fuer EHC: ENTSCHIEDEN

## Aktueller Live-Stand (25.03.2026)
- URL: https://bright-cannoli-eeaa45.netlify.app (Login: EHC2026)
- Interface zeigt 4-Spalten-Layout: Ordner | Mail-Liste | Mail-Inhalt | KI-Panel
- Echte Outlook-Ordner, echte Mails, echte Graph API-Anbindung
- KI-Analyse, Aufgaben, Ablegen, Antwort, Feedback, Wiederkehrend - alles gebaut
- Deployment von preview6.html ist heute (25.03) erledigt worden

## Microsoft 365 Setup (EHC)
- Postfach: o.reinpold@hernie.de auf Microsoft 365 Business Standard
- MX-Record bleibt bei all-inkl (Mitarbeiter unberuehrt)
- Weiterleitung: all-inkl -> Microsoft 365 als Kopieempfaenger
- SPF: v=spf1 a mx include:spf.kasserver.com include:spf.protection.outlook.com ~all
- Internal Relay: konfiguriert (hernie.de nicht autoritaetiv)
- OneDrive: C:\Users\Startklar\OneDrive - Elbe Hernien Centrum EHC GmbH

## OneDrive Ordnerstruktur (fuer Anhang-Ablage)
EHC: Eingangsrechnungen, Vertraege, Korrespondenz, Personal, Finanzen, OP-Dokumentation
Qodia: Allgemein, Investoren, Vertraege
Privat: Allgemein
Kein Anhang

## Prioritaetssystem
Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten

## Dateiformat Anhaenge
JJMMTT_Organisation_Dateiname.ext (z.B. 260324_Helios_Kliniken_Rechnung_2026-0342.pdf)