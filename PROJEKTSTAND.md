# KI Mail Assistent – Projektstand

## Kontext
- **Ole Reinpold** – GF Elbe Hernien Centrum EHC GmbH + Qodia GmbH
- E-Mail: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Ansprache: Du | Sprache: Deutsch | Ole navigiert selbst, Claude gibt Anweisungen

## Ziel
Morgens Interface öffnen → alle neuen Mails sehen → KI-Analyse lesen → mit einem Klick:
- Mail in Outlook-Ordner verschieben
- Anhang in OneDrive ablegen (Format: JJMMTT_Organisation_Dateiname.ext)
- Antwort direkt in Outlook öffnen (mailto-Link)
- Feedback an Claude geben (Sterne + Text) damit System lernt

**Prioritätssystem:** Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten

## Tech Stack
- **Frontend:** HTML + CSS + Vanilla JS → Netlify
- **Repo:** github.com/olereinpold92/ki-mail-assistent
- **Dateien:** index.html (Shell) + app.js (Logik) + netlify.toml (CSP-Header)
- **Live URL:** https://bright-cannoli-eeaa45.netlify.app
- **Login-Passwort:** EHC2026
- **GitHub Token:** In 1Password gespeichert unter "ki-mail-assistent GitHub Token" (no expiry)

## Power Automate Flow
- Flow ID: 6ce87867-8356-4683-b44a-6d3157347227
- Trigger: neue Mail bei o.reinpold@hernie.de
- Aktion: Claude API (claude-sonnet-4-6) analysiert Mail → JSON zurück
- Status: LÄUFT – aber Ergebnis wird noch nirgends gespeichert
- Claude Prompt: Analysiere E-Mail auf Deutsch, gib JSON zurück mit prioritaet, aktion, antwortvorschlag, email_ordner, onedrive_ordner, weitere_aktionen, begruendung

## Azure App Registration
- Name: KI Mail Assistent EHC
- Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Redirect URI: https://bright-cannoli-eeaa45.netlify.app (SPA)

**API-Berechtigungen (Microsoft Graph, delegiert):**
- User.Read: OK
- Mail.ReadWrite: OK (gesetzt, Admin-Zustimmung noch ausstehend)
- Files.ReadWrite: FEHLT
- Administratorzustimmung erteilen: FEHLT

## Offene Punkte (in dieser Reihenfolge)
1. Azure: Files.ReadWrite setzen, dann Administratorzustimmung erteilen
2. MSAL.js in app.js einbauen, "Mit Microsoft anmelden" Button
3. Echte Mails via Microsoft Graph API laden statt Demo-Daten
4. Mail verschieben + Anhang in OneDrive ablegen via Graph API
5. Power Automate: Claude-Analyse ins Interface bringen

## M365 / Outlook Setup
- MX-Record unverändert (all-inkl.), Weiterleitung zu Microsoft 365 aktiv
- OneDrive Pfad: C:\Users\Startklar\OneDrive - Elbe Hernien Centrum EHC GmbH

## OneDrive Ordner (Dropdown im Interface)
EHC: Eingangsrechnungen, Vertraege, Korrespondenz, Personal, Finanzen, OP-Dokumentation
Qodia: Allgemein, Investoren, Vertraege | Privat: Allgemein | Sonstiges: Kein Anhang

## Zusammenarbeit
- Ole navigiert selbst, Claude gibt Schritt-fuer-Schritt-Anweisungen
- Code-Updates laufen ueber GitHub API direkt (Token aus 1Password)
- Screenshots nur wenn noetig
