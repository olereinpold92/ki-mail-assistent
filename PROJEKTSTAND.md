# KI Mail Assistent – Projektstand

## Kontext & Person
- Ole Reinpold, Du-Ansprache, Deutsch
- Prokurist/GF: Elbe Hernien Centrum EHC GmbH (kurz: EHC)
- Mitgruender/GF: Qodia GmbH
- E-Mail: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- Arbeitsstil: Ole navigiert selbst, Claude gibt direkte Schritt-fuer-Schritt-Anweisungen

## Langfristiges Ziel
E-Mail ist Schritt 1 zur vollstaendigen Automatisierung des Arbeitsalltags.
Danach: Kalender, Dokumente, Aufgaben, Buchhaltung etc.

## KI Mail Assistent – Ziel
- Jeden Morgen Interface oeffnen
- Alle neuen Mails sehen + KI-Analyse (Prioritaet, Aktion, Antwortvorschlag, Begruendung)
- Mit einem Klick: antworten, Anhang in OneDrive ablegen, Mail in Outlook-Ordner verschieben
- Feedback (Sterne + Text) damit System lernt
- Dateiformat: JJMMTT_Organisation_Dateiname.ext
- Prioritaeten: Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten

## Tech Stack
- HTML + CSS + Vanilla JS (keine Frameworks)
- GitHub: olereinpold92/ki-mail-assistent
- Netlify: https://bright-cannoli-eeaa45.netlify.app / Login: EHC2026
- Dateien: index.html, app.js, netlify.toml
- Code-Updates immer direkt ueber GitHub API (Token ohne Ablauf), nie ueber Browser-Editor

## Azure / Microsoft
- App: KI Mail Assistent EHC
- Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Redirect URI: https://bright-cannoli-eeaa45.netlify.app (Typ: SPA)
- Berechtigungen: User.Read (ok), Mail.ReadWrite (ok), Files.ReadWrite (FEHLT), Administratorzustimmung (FEHLT)

## Power Automate
- Flow ID: 6ce87867-8356-4683-b44a-6d3157347227
- Trigger: neue Mail an o.reinpold@hernie.de
- Aktion: Claude API (claude-sonnet-4-6) analysiert Mail, gibt JSON zurueck
- JSON-Felder: prioritaet, aktion, antwortvorschlag, email_ordner, onedrive_ordner, begruendung
- Status: laeuft, aber Ergebnis wird noch nicht gespeichert/angezeigt

## OneDrive Ordnerstruktur (Dropdown im Interface)
EHC: Eingangsrechnungen, Vertraege, Korrespondenz, Personal, Finanzen, OP-Dokumentation
Qodia: Allgemein, Investoren, Vertraege
Privat: Allgemein
Kein Anhang

## Naechste Schritte (Prioritaet)
1. Azure: Files.ReadWrite hinzufuegen + Administratorzustimmung erteilen
2. app.js: OAuth Implicit Flow (kein MSAL noetig) einbauen – Microsoft verbinden Button
3. Echte Mails via Microsoft Graph API laden statt Demo-Daten
4. Mail verschieben + Anhang in OneDrive ablegen via Graph API
5. Power Automate Analyse ins Interface bringen

## So startest du einen neuen Chat
Schreib: "Lies PROJEKTSTAND.md aus github.com/olereinpold92/ki-mail-assistent und mach weiter"
