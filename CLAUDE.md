# CLAUDE.md – KI Mail Assistent für Ole Reinpold (EHC Hamburg)

Lies diese Datei IMMER komplett bevor du irgendetwas tust.

## Wer ist Ole?
- Ole Reinpold, Ansprache: Du, Sprache: immer Deutsch
- Prokurist/GF: Elbe Hernien Centrum EHC GmbH (Hamburger Hernien Centrum), ~8 Mitarbeiter, Hernienchirurgie
- Mitgründer/GF: Qodia GmbH (KI-Lösungen GOÄ-Abrechnung), 4 Gründer
- Kein Entwickler. Technikaffinität 6-7/10. Braucht klare Anweisungen ohne Fachjargon.
- Will als Sparringspartner gefordert werden – challenge Ole aktiv wenn er auf dem falschen Weg ist.
- Langfristiges Ziel: Gesamten Arbeitsalltag automatisieren. E-Mail ist Schritt 1.

## Wie wir zusammenarbeiten (IMMER einhalten)
- Erkläre jeden Schritt klar bevor du ihn ausführst
- Zeige Code-Änderungen zur Review bevor du sie speicherst – frage: "Soll ich das so umsetzen?"
- Wenn Ole sagt "Stopp" oder "warte" – sofort aufhören, nicht weitermachen
- Wenn du unsicher bist: sag es direkt, recherchiere, gib dann eine klare Empfehlung
- Triff keine Annahmen über was Ole will – frag lieber einmal zu viel
- Nach jeder Session: CLAUDE.md und PROJEKTSTAND.md aktualisieren

## Was dieses Projekt ist
Ein KI-gesteuerter E-Mail-Assistent der Ole hilft, seine täglichen E-Mails schnell abzuarbeiten.

### Was der Assistent pro Mail tut:
1. Priorität vorschlagen: Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten
2. Antwortvorschlag generieren (in Oles Stil, auf Deutsch, bearbeitbar)
3. E-Mail-Ordner vorschlagen (wo die Mail in Outlook abgelegt werden soll)
4. Anhänge in OneDrive ablegen: Format JJMMTT_Organisation_Dateiname.ext
5. Aufgabenliste: Nur was ÜBER Antworten+Ablegen hinausgeht. Nicht kleinteilig. Keine Ablage-Aufgaben. Max 3.
6. Feedback-System: "Alles 100% korrekt" oder "Nicht korrekt" + Freitext. KI lernt daraus UND aus manuellen Anpassungen.
7. Wiederkehrende Mails: Toggle + Intervall, System merkt sich Einstellungen

### Entschiedene UI-Regeln:
- keine_antwort_noetig: true bei Rechnungen, Newslettern, Infomails
- Antwort als Toggle (Ja/Nein), nicht als Button
- Aufgaben: nie kleinteilig, nie "Beleg ablegen" wenn Anhang ohnehin abgelegt wird
- KI-Analyse standardmässig zugeklappt (bei Bedarf aufklappbar)

## Tech Stack
- Alles in EINER index.html (kein separates app.js)
- GitHub Repo: olereinpold92/ki-mail-assistent
- Netlify: https://bright-cannoli-eeaa45.netlify.app / Login: EHC2026
- Netlify Pro Plan (1000 Build-Credits/Monat) – sparsam einsetzen!
- Azure Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Azure Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Azure Redirect URI: https://bright-cannoli-eeaa45.netlify.app/ (SPA, Implicit Flow aktiv)
- Azure Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite – alle erteilt

## Microsoft 365 Setup
- Postfach: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- MX-Record bleibt bei all-inkl (Mitarbeiter unberührt)
- Weiterleitung: all-inkl → Microsoft 365 als Kopieempfänger
- SPF: v=spf1 a mx include:spf.kasserver.com include:spf.protection.outlook.com ~all
- Internal Relay konfiguriert in Exchange
- OneDrive: C:\Users\Startklar\OneDrive - Elbe Hernien Centrum EHC GmbH

## OneDrive Ordnerstruktur
EHC: Eingangsrechnungen, Verträge, Korrespondenz, Personal, Finanzen, OP-Dokumentation
Qodia: Allgemein, Investoren, Verträge
Privat: Allgemein
Kein Anhang

## Deploy-Workflow
- Änderungen in index.html lokal speichern
- In GitHub Desktop: Commit + Push
- In Netlify: Deploys → "Trigger deploy" manuell auslösen
- Danach: Auto-Deploy sofort wieder deaktivieren
- NIEMALS direkt auf main pushen ohne dass Ole die Änderung gesehen hat

## Was aktuell deployed ist (Stand 25.03.2026)
Die Live-Seite zeigt noch einen älteren Stand. Die fertige preview6.html mit allen Features wurde noch nicht korrekt deployed.

### Was in preview6.html fertig ist (17 Features):
1. 4-Spalten-Layout: Ordner-Sidebar | Mail-Liste | Mail-Inhalt | KI-Panel
2. Verschiebbare Spaltenbreiten (Drag-to-resize), Einstellung wird gespeichert
3. Alle Spalten auf/zuklappbar, Einstellung wird gespeichert
4. Prio manuell anpassbar (5 Buttons)
5. KI-Analyse einklappbar (standardmässig zu)
6. Aufgabenliste mit Checkbox + eigene Aufgaben hinzufügbar
7. Ablegen-Bereich: Mail verschieben + Anhänge mit editierbarem Dateinamen + Ordner-Selector + Neuer Unterordner
8. Antwort als Toggle (Ja/Nein)
9. Feedback: Alles korrekt / Nicht korrekt + Freitext
10. Wiederkehrende Mails: Toggle + Intervall
11. "Alles bestätigen & ausführen": Ein Klick macht alles
12. Echte Outlook-Ordner laden via Graph API
13. Klick auf Ordner lädt Mails aus diesem Ordner
14. Mail wirklich verschieben via Graph API
15. OneDrive-Ordner laden (echte Struktur im Dropdown)
16. Anhang in OneDrive ablegen (echte Upload-Funktion)
17. KI lernt aus Anpassungen UND Feedback via localStorage

## Erste Aufgabe in dieser Session
Lies zuerst die aktuelle index.html im Repo. Dann zeige Ole was der aktuelle Stand ist und was als nächstes ansteht. Frag ihn bevor du irgendetwas änderst.

## Entschiedene Punkte – nicht nochmal diskutieren
- Claude Code wurde als Entwicklungsumgebung gewählt (statt Browser-Chat) wegen Kontextverlust-Problem
- n8n/Make/Power Automate: verworfen, direkte Graph API ist besser
- Ein-Datei-Ansatz (alles in index.html): beibehalten
- App-Passwort: EHC2026
- Architektur (GitHub + Netlify + Graph API + Claude API im Browser): bestätigt richtig