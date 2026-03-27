# KI Mail Assistent – Projektstand (26.03.2026, 20:30 Uhr)

## STRATEGIEWECHSEL: Outlook Add-in statt Web-App
Am 25.03.2026 entschieden: Outlook Add-in statt eigener Web-App.
Grund: Web-App versuchte Outlook nachzubauen, scheiterte an Graph API Bug.
Add-in laeuft direkt IN Outlook als Seitenleiste.

## Aktueller Stand: Add-in laeuft, Grundfunktionen getestet

### Was FUNKTIONIERT (getestet am 26.03.2026):
- Add-in laeuft in neuem Outlook und altem Outlook
- Claude API Key eingetragen, KI-Analyse funktioniert
- Microsoft-Verbindung (MSAL/OAuth) funktioniert, Token wird gecacht
- Mail-Analyse: Aktion, Ordner, Antwort, Aufgaben werden von KI vorgeschlagen
- Aktions-Buttons: Sofort, Erledigen, ToDo Wichtig, ToDo NTH, Nachhalten, Ablage, Loeschen
- Mail verschieben in Outlook-Ordner (funktioniert wenn Ordner schon Mails enthalten hat)
- OneDrive-Browser: Ordnerstruktur wird echt geladen, navigierbar, Suche mit Pfad-Anzeige
- Anhang in OneDrive hochladen (funktioniert)
- Antwort in Outlook oeffnen (Reply, Reply All, Forward) – NIE automatisch senden
- Microsoft To Do Integration: Aufgaben erstellen (Tasks.ReadWrite Berechtigung erteilt)
- Feedback-System: Toggle korrekt/nicht korrekt + Freitextfeld
- "Alles bestaetigen & ausfuehren" Button (fuehrt alle Aktionen aus)
- Domain-Sperren Toggle (erscheint nur bei Aktion "Loeschen")
- Lern-System: Absender-Domain + Betreff-Stichworte → Ordner-Zuordnung
- MSAL.js lokal eingebunden (kein CDN-Problem mehr)
- Auto-Reconnect beim Reload (Token aus Cache)

### Was NICHT richtig funktioniert / bekannte Bugs:
- Add-in schliesst sich bei Mail-Wechsel (Microsoft Pinning-Bug, nicht loesbar)
  → Workaround: Schneller Reload, Auto-Reconnect, Cache
- Outlook Mail-Ordner Unterordner: Graph API childFolders Bug (liefert 0 Ergebnisse)
  → Workaround: Feste Ordnerliste im Code (FOLDER_STRUCTURE), manuell erweiterbar via "+ Ordner"
- Folder-IDs werden per Rueckwaerts-Suche gefunden (Ordner muss mind. 1 Mail enthalten)
  → Leere Ordner koennen nicht als Ziel verwendet werden bis erste Mail manuell verschoben
- Breite der Add-in Seitenleiste im neuen Outlook nicht aenderbar (Microsoft-Limitation)
- "Alles bestaetigen & ausfuehren": Moeglicherweise werden nicht alle Aktionen korrekt ausgefuehrt
  → Muss noch systematisch getestet werden (Anhaenge-Upload, To Do Erstellung)
- Forward-Funktion: Erstellt Entwurf, oeffnet kein natives Forward-Fenster
- Antwort-Textfelder: Expandieren/Collapsieren muss noch geprueft werden
- KI-Analyse muss manuell ausgeloest werden ("Jetzt analysieren" Button)
  → Kostenschutz: Kein Auto-Analyse, keine Doppel-Analyse, Warnung bei alten Mails

### Was noch NICHT gebaut ist:
- KI lernt aus manuellen Mail-Verschiebungen (wenn User Mail selbst verschiebt)
- Wiederkehrende Mails: Toggle + Intervall
- KI-Stil-Training aus echten Antworten (Kommunikationsstil lernen)
- Automatische Neue-Mail-Erkennung (optional fuer spaeter)

## Aktions-System (Stand 26.03.2026)

### Aktions-Buttons (Prioritaet/Ziel):
| Button | Ziel-Ordner | Verhalten |
|--------|------------|-----------|
| Sofort | bleibt im Posteingang | Keine Verschiebung |
| Erledigen | bleibt im Posteingang | Keine Verschiebung |
| ToDo Wichtig | 01_ToDo / 02_Wichtig | Mail wird verschoben |
| ToDo NTH | 01_ToDo / 04_NTH | Mail wird verschoben |
| Nachhalten | 02_Nachhalten | Mail wird verschoben |
| Ablage | KI waehlt passenden Ordner | Mail wird verschoben |
| Loeschen | Geloeschte Elemente | Mail wird verschoben + Domain-Sperren Toggle |

### Einzel-Aktionen:
| Aktion | Button | Verhalten |
|--------|--------|-----------|
| Mail verschieben | "Mail verschieben" | Verschiebt in gewaehlten Ordner |
| Anhang ablegen | "Hier ablegen" | Upload in ausgewaehlten OneDrive-Ordner |
| Antwort | "Antworten" / "Allen antworten" / "Weiterleiten" | Oeffnet in Outlook, NIE auto-senden |
| Aufgabe | "In Microsoft To Do erstellen" | Erstellt Task mit Link zur Mail |
| Feedback | Toggle + Textfeld | Speichert in Lern-System |

### "Alles bestaetigen & ausfuehren":
1. Mail in Ordner verschieben
2. Anhaenge in OneDrive ablegen
3. Aufgaben in Microsoft To Do erstellen
4. Antwort in Outlook oeffnen (Reply All, NIE auto-senden)
5. Feedback speichern

## Outlook Mail-Ordner (fest im Code hinterlegt)
Posteingang mit Unterordnern:
- 00_Archiv (Circle Health, GuadelajARTE, Hernien Klinik, Hernienzentrum Koeln, Klinzing, kv-abrechnungspruefung, Nasenzentrum Sued-West, TrainerVenue)
- 01_ToDo (01_Wichtig & Dringend, 02_Wichtig (Website), 03_Muss gemacht werden, 04_NTH)
- 02_Nachhalten
- BAG
- Business Development (Freelancer, PXA)
- Controlling
- Finanzbuchhaltung
- Firmen & Organisationen (Abrechnung, ATOS, Behoerden, Bestellungen, Elbklinik, FAK, Hafenklinik, Helios, Krankenkassen, Reisen, Versicherung)
- Hanse
- Hernia Consult
- Hernienmissionen
- HHC
- Hospitationen
- IT (Anleitungen)
- Kommunikation (hernie.de, hernie.net)
- KV
- Newsletter
- Personal (Bewerbungen, Offen)
- Persoenliches
- Politik
- Prozesse
- Rechtliches
- Sonstiges
- Strategie
- Wolle

Systemordner: Archiv, Entwuerfe, Geloeschte Elemente, Gesendete Elemente, Junk-E-Mail, Papierkorb

## Dateistruktur
```
ki-mail-assistent/
├── manifest.xml              ← Outlook Add-in Manifest
├── addin/
│   ├── taskpane.html         ← HAUPTDATEI: alles drin (HTML+CSS+JS, ~2500 Zeilen)
│   ├── msal-browser-3.27.0.min.js ← MSAL lokal (kein CDN)
│   ├── icon-16/32/64/80/128.png
├── gedaechtnis/
│   ├── _config.json
│   ├── profil/grundprofil.md
│   ├── regeln/ordner.json, anhaenge.json, antworten.json
│   ├── kontakte/ beispiele/ feedback/
├── certs/localhost.crt + .key
├── server.py                 ← Python HTTPS-Server
├── start-addin.bat           ← Doppelklick = Server starten
├── index.html                ← ALTE Web-App (Referenz)
├── CLAUDE.md
├── KONZEPT.md                ← Hintergrund, Zielsetzung, Vision
└── PROJEKTSTAND.md           ← Diese Datei
```

## Wie man das Add-in startet
1. Doppelklick auf `start-addin.bat`
2. Outlook oeffnen (neues Outlook empfohlen)
3. Mail anklicken → "KI Mail Assistent" im Ribbon klicken
4. Beim ersten Mal: "Einstellungen" → Claude API Key eintragen
5. "Verbinden" → Microsoft OAuth Login

## Azure Konfiguration
- Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Redirect URIs (SPA): http://localhost:8080, https://localhost:3000, https://localhost:3000/addin/taskpane.html
- Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite, Tasks.ReadWrite – alle erteilt
- FEHLEND: MailboxSettings.ReadWrite – noetig fuer Sperren-Feature (Posteingangsregeln erstellen)

## Entschiedene Punkte – NICHT nochmal diskutieren
- Outlook Add-in statt Web-App: ENTSCHIEDEN (25.03.2026)
- n8n/Make/Power Automate: VERWORFEN
- Netlify: NUR NOCH ALTLAST
- Microsoft 365 als Mail-Hub: ENTSCHIEDEN
- Claude Code als Entwicklungsumgebung: ENTSCHIEDEN
- Ein-Datei-Ansatz (taskpane.html): BEIBEHALTEN
- Claude API Key im localStorage: akzeptiertes Risiko
- Add-in Pinning nicht loesbar: AKZEPTIERT (Microsoft-Bug)
- Mail-Ordner fest im Code: AKZEPTIERT (Graph API childFolders Bug)
- OneDrive-Ordner per Graph API: FUNKTIONIERT (kein Bug wie bei Mail-Ordnern)
- Antworten NIE automatisch senden: IMMER nur in Outlook oeffnen
- Microsoft To Do fuer Aufgaben: ENTSCHIEDEN, parallel zu E-Mail-Ordner-System
- API-Kostenschutz: Analyse nur manuell, nie automatisch, nie doppelt (Ole hat Auto-Analyse getestet und wieder deaktiviert)

## Session 27.03.2026: KI-Chat, Persistenz, Sperren-Feature

### Neue Features
- **KI-Chat**: "KI fragen" Bereich – Fragen zur aktuellen Mail stellen, mit Dokumenten-Suche
  - Tool Use: KI kann selbststaendig Mails in Outlook-Ordnern durchsuchen
  - PDF-Analyse: Anhaenge werden direkt an Claude geschickt und gelesen
  - Vollbild-Modus fuer laengere Diskussionen
  - "Antwort daraus formulieren" Button: Erstellt Mail-Entwurf basierend auf Chat
- **Server.py erweitert**: POST-Endpunkt fuer Gedaechtnis-Dateien (Whitelist)
- **Persistenz**: Feedback, Analysis-Log und Chat-Verlaeufe werden auf Festplatte gespeichert
- **Chat-Prompt**: KI als Sparringspartner (challengen, nicht nach dem Mund reden)
- **Sperren-Buttons**: Zwei Buttons oben im Add-in: "Sperren: absender@..." und "Sperren: @domain"
  - Erstellt Posteingangsregel in Microsoft 365 (kontogebunden, nicht nur lokal)
  - Verschiebt aktuelle Mail in Junk-E-Mail
- **Abmelden-Button**: Im Header, loescht MSAL-Cache komplett (kein Browser-Umweg noetig)
- **Antwort-Modus als Auswahl**: Antworten/Allen antworten/Weiterleiten als Toggle-Buttons statt direkte Aktion
- **Aufgaben editierbar**: Tasks koennen bearbeitet und geloescht werden

### Offene Bugs (DRINGEND, als naechstes fixen)
1. **Microsoft Login Popup oeffnet sich im Browser statt im Add-in**: Das Popup-Fenster
   zeigt "localhost hat die Verbindung verweigert" wenn das selbstsignierte Zertifikat
   im Browser nicht akzeptiert wurde. Einmalig https://localhost:3000 im Browser oeffnen
   und Zertifikat akzeptieren. LANGFRISTIGE LOESUNG: Office.context.ui.displayDialogAsync
   verwenden statt window.open fuer den Login.
2. **Sperren-Feature braucht MailboxSettings.ReadWrite Berechtigung**: Muss in Azure Portal
   hinzugefuegt und Admin-Consent erteilt werden. Alternativ: Regel nur lokal speichern
   und manuell in Outlook-Regeln anlegen.
3. **Mail wird nicht in gewaehlten Ordner verschoben**: Bei Aktion "sofort"/"erledigen"
   wird die Mail nie verschoben, auch wenn ein Ordner explizit gewaehlt wurde. Fix:
   Verschiebung ausfuehren wenn ein Ordner eingetragen ist, egal welche Aktion.
4. **OneDrive-Upload bei "Alles ausfuehren"**: Muss getestet werden ob Anhaenge korrekt
   in den ausgewaehlten OneDrive-Ordner hochgeladen werden.
5. **Felder werden zurueckgesetzt bei UI-Interaktion**: Wenn man in ein Textfeld klickt,
   werden andere Sektionen automatisch zugeklappt (expandField-Problem).

## Gedaechtnis-Architektur: Umbau auf Tag-System (entschieden 26.03.2026)
- **Alt**: Ordner-Hierarchie (profil/, regeln/, kontakte/) mit "immer" oder "bei_bedarf"
- **Neu**: Flache entries.json mit Tags + selektivem Tag-Matching
- **Zwei Ebenen**: Systemverhalten (fest im Prompt) vs. Gelerntes Wissen (in entries.json)
- **Details**: Siehe KONZEPT.md Abschnitt 5
- **Status**: Konzept fertig, Umsetzung begonnen

## Vision: Persoenlicher KI-Assistent
- Ebene 1 (jetzt): Muster-Erkennung (Ordner-Zuordnung, Dateinamen, Prios)
- Ebene 2 (Wochen): Kommunikationsstil lernen aus echten Antworten
- Ebene 3 (Monate): Strategischer Berater
Alles gespeichert in /gedaechtnis/ – portabel, nicht an Anthropic gebunden.
