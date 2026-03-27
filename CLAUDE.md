# CLAUDE.md – KI Mail Assistent (Tool-spezifisch)

Lies ZUERST die shared-path.config in diesem Repo – der Pfad dort zeigt auf das ehc-shared Repo.
Lies dort CLAUDE.md (KOMPLETT – enthaelt kritische Arbeitsregeln zu Feedback, Dokumentation, Git).
Lies dort KONZEPT.md und PROJEKTSTAND.md fuer den Gesamtkontext.
Lies DANACH diese Datei fuer Mail-Assistent-spezifische Regeln.

## Was dieses Projekt ist
Ein Outlook Add-in das als Seitenleiste in Outlook laeuft und Ole hilft, seine E-Mails schneller abzuarbeiten.
Es nutzt ein geteiltes "Gedaechtnis" (Textdateien in ehc-shared/gedaechtnis/) das der KI bei jeder Analyse mitgegeben wird.

### Was der Assistent pro Mail tut:
1. Aktion vorschlagen: Sofort / Erledigen / ToDo Wichtig / ToDo NTH / Nachhalten / Ablage / Loeschen
2. Ordner vorschlagen (wo die Mail in Outlook abgelegt werden soll)
3. Antwortvorschlag generieren (in Oles Stil, auf Deutsch, bearbeitbar)
4. Anhaenge in OneDrive ablegen: Format JJMMTT_Organisation_Dateiname.ext
5. Aufgaben in Microsoft To Do erstellen (nur was UEBER Antworten+Ablegen hinausgeht, max 3)
6. Feedback-System: Toggle korrekt/nicht korrekt + Freitext, KI lernt daraus

### Aktions-Buttons:
| Button | Ziel-Ordner |
|--------|------------|
| Sofort | bleibt im Posteingang |
| Erledigen | bleibt im Posteingang |
| ToDo Wichtig | 01_ToDo / 02_Wichtig |
| ToDo NTH | 01_ToDo / 04_NTH |
| Nachhalten | 02_Nachhalten |
| Ablage | KI waehlt passenden Ordner |
| Loeschen | Geloeschte Elemente + Domain-Sperren Toggle |

### Entschiedene UI-Regeln:
- keine_antwort_noetig: true bei Rechnungen, Newslettern, Infomails
- Antwort als Toggle (Ja/Nein), drei Buttons: Antworten / Allen antworten / Weiterleiten
- Aufgaben: nie kleinteilig, nie "Beleg ablegen" wenn Anhang ohnehin abgelegt wird
- KI-Analyse standardmaessig zugeklappt
- Domain-Sperren Toggle nur sichtbar wenn Aktion "Loeschen" gewaehlt
- Antwort NIE automatisch senden – IMMER in Outlook oeffnen (Reply All als Standard)
- API-Kostenschutz: Analyse nur manuell, nie automatisch, nie doppelt
- WICHTIG: Niemals E-Mails automatisch senden – IMMER nur in Outlook oeffnen

## Architektur: Outlook Add-in
- Outlook Add-in (Seitenleiste) statt eigener Web-App
- Alles in EINER taskpane.html (HTML + CSS + JS, ~3300 Zeilen)
- Lokaler HTTPS-Server (Python, Port 3000) – kann lesen UND schreiben
- MSAL.js lokal eingebunden (nicht ueber CDN)
- manifest.xml fuer Outlook Sideloading
- Gedaechtnis liegt in ehc-shared/gedaechtnis/ (Pfad via shared-path.config)
- server.py leitet /gedaechtnis/-Anfragen auf das Shared-Verzeichnis um
- KI-Chat: Diskussion mit KI ueber Mails, inkl. Dokumenten-Suche via Tool Use

## Azure Konfiguration
- Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Redirect URIs (SPA): http://localhost:8080, https://localhost:3000, https://localhost:3000/addin/taskpane.html
- Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite, Tasks.ReadWrite – alle erteilt
- FEHLEND: MailboxSettings.ReadWrite – noetig fuer Sperren-Feature (Posteingangsregeln)

## Microsoft 365 Setup
- Postfach: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- MX-Record bleibt bei all-inkl (Mitarbeiter unberuehrt)
- OneDrive: C:\Users\Startklar\OneDrive - Elbe Hernien Centrum EHC GmbH

## Wie man das Add-in startet
1. start-addin.bat doppelklicken (startet HTTPS-Server auf Port 3000)
2. Outlook oeffnen (neues Outlook empfohlen), Mail anklicken
3. "KI Mail Assistent" Button im Ribbon klicken
4. Beim ersten Mal: Claude API Key in Einstellungen eintragen
5. "Verbinden" klicken fuer Microsoft OAuth

## Bekannte Limitierungen (NICHT nochmal versuchen zu loesen)
- Add-in Pinning funktioniert nicht (Microsoft-Bug, beide Outlook-Versionen)
- Graph API childFolders Bug: Unterordner von Posteingang werden nicht geliefert
  → Mail-Ordner sind fest im Code als FOLDER_STRUCTURE hinterlegt
  → Neue Ordner ueber "+ Ordner" Button manuell hinzufuegen
- Folder-ID wird per Rueckwaerts-Suche gefunden (Ordner muss mind. 1 Mail enthalten)
- Breite der Seitenleiste im neuen Outlook nicht aenderbar
- OneDrive-Ordner per Graph API funktionieren OHNE Bug

## Entschiedene Punkte – nicht nochmal diskutieren
- Outlook Add-in statt Web-App: ENTSCHIEDEN (25.03.2026)
- n8n/Make/Power Automate: VERWORFEN
- Ein-Datei-Ansatz (taskpane.html): BEIBEHALTEN
- Claude API Key im localStorage: akzeptiertes Risiko
- Microsoft To Do fuer Aufgaben: ENTSCHIEDEN (parallel zu E-Mail-Ordner-System)
- Antworten NIE automatisch senden: IMMER nur in Outlook oeffnen
