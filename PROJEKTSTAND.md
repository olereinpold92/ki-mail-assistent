# KI Mail Assistent – Projektstand (25.03.2026)

## Kontext & Person
- Ole Reinpold, Du-Ansprache, kein Techniker
- GF: Elbe Hernien Centrum EHC GmbH + Qodia GmbH
- o.reinpold@hernie.de (Microsoft 365)

## Tech Stack
- Alles in einer index.html (HTML/CSS/Vanilla JS)
- GitHub: olereinpold92/ki-mail-assistent (Token in 1Password)
- Netlify: https://bright-cannoli-eeaa45.netlify.app / Login: EHC2026
- Auto-Deploy aktiv, Build-Credits fast aufgebraucht – sparsam deployen!
- Azure Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Azure Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f

## Deploy-Workflow (EINZIGER zuverlaessiger Weg)
1. Claude baut index.html und stellt sie als Download bereit
2. Ole laedt sie herunter
3. github.com/olereinpold92/ki-mail-assistent → Add file → Upload files
4. Datei als index.html hochladen → Commit changes
5. Netlify deployed automatisch (1-2 Min)

## Entschiedene Punkte – NICHT nochmal diskutieren
- Claude Code: ABGELEHNT. Ole ist kein Entwickler.
- Deploy NUR ueber GitHub Upload (s.o.) – nicht ueber Browser-JS (10KB-Limit)
- Ein-Datei-Ansatz beibehalten
- App-Passwort: EHC2026

## Aktueller Stand (25.03.2026)
- preview6.html ist live deployed
- 4-Spalten-Layout, echte Graph API, KI-Analyse, Aufgaben, Ablegen, Antwort, Feedback, Lernen

## Gedaechtnis zwischen Chats
Claude hat kein Gedaechtnis. Jeden Chat mit: Lies PROJEKTSTAND.md starten.
Alle Entscheidungen hier dokumentieren.

## OneDrive Ordner
EHC: Eingangsrechnungen, Vertraege, Korrespondenz, Personal, Finanzen, OP-Dokumentation
Qodia: Allgemein, Investoren, Vertraege | Privat: Allgemein | Kein Anhang

## Prioritaeten
Wichtig & Dringend / Wichtig / Muss / Nice to have / Nachhalten

## Dateiformat Anhaenge
JJMMTT_Organisation_Name.ext