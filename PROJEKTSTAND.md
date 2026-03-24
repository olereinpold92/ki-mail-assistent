# KI Mail Assistent – Projektstand

## Kontext & Person
- Ole Reinpold, Du-Ansprache, Deutsch
- Prokurist/GF: Elbe Hernien Centrum EHC GmbH (kurz: EHC)
- Mitgruender/GF: Qodia GmbH
- E-Mail: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- Arbeitsstil: Ole macht einfache Klicks selbst, Claude uebernimmt komplexe Konfigurationen und Code.

## Langfristiges Ziel
E-Mail ist Schritt 1 zur vollstaendigen Automatisierung des Arbeitsalltags.

## KI Mail Assistent – Ziel
- Jeden Morgen Interface oeffnen, neue Mails sehen, KI-Analyse lesen
- Pro Mail: Prioritaet, Aktion, Antwortvorschlag, Begruendung
- Mit einem Klick: antworten, Anhang in OneDrive, Mail in Outlook-Ordner
- Feedback (Sterne + Text) zum KI-Training
- Dateiformat: JJMMTT_Organisation_Dateiname.ext
- Prioritaeten: Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten

## Tech Stack
- HTML + CSS + Vanilla JS, GitHub: olereinpold92/ki-mail-assistent
- Netlify: https://bright-cannoli-eeaa45.netlify.app / Login: EHC2026
- Dateien: index.html, app.js, netlify.toml
- GitHub Token: in 1Password gespeichert (kein Ablauf)
- WICHTIG: Netlify Auto-Deploy ist DEAKTIVIERT. Nach Code-Push manuell deployen: Netlify -> Deploys -> Trigger deploy

## Azure / Microsoft
- App: KI Mail Assistent EHC
- Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Redirect URI: https://bright-cannoli-eeaa45.netlify.app/ (SPA)
- Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite + Adminzustimmung erteilt

## Aktueller Stand (24.03.2026)
- Login (EHC2026) funktioniert
- Microsoft OAuth funktioniert, Token in sessionStorage
- Echte Mails laden via Graph API
- CSP in netlify.toml erlaubt graph.microsoft.com und api.anthropic.com

## Offene Punkte – naechste Session
1. BUG: KI-Features (Antwort, Analyse) funktionieren nur bei einer Mail – escId()-Problem mit langen Graph IDs
2. UI komplett ueberarbeiten – besseres Design und Layout
3. KI-Analyse beim Laden verbessern
4. Mail in Outlook-Ordner verschieben via Graph API
5. Anhang in OneDrive ablegen via Graph API

## Neuen Chat starten
Lies PROJEKTSTAND.md und app.js aus github.com/olereinpold92/ki-mail-assistent und mach weiter.
