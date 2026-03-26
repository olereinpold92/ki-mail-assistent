# KONZEPT.md – KI Mail Assistent: Gesamtkonzept & Projektgedaechtnis

Dieses Dokument haelt ALLES fest was wir ueber Hintergrund, Ziele, Strategie und Vorgehen besprochen haben.
Es ist das Projektgedaechtnis fuer alle zukuenftigen Sessions.

---

## 1. HINTERGRUND: Warum dieses Projekt?

### Das Problem
Ole Reinpold ist Geschaeftsfuehrer/Prokurist von zwei Unternehmen:
- **Elbe Hernien Centrum EHC GmbH** (Hamburger Hernien Centrum) – Hernienchirurgie, ~8 Mitarbeiter, Standort Wentorf bei Hamburg
- **Qodia GmbH** – KI-Loesungen fuer GOAe-Abrechnung, 4 Gruender

Als GF beider Firmen bearbeitet Ole taeglich eine grosse Menge E-Mails. Die Bandbreite reicht von:
- Klinik-Betrieb (Operationsplanung, Mitarbeiter, Versicherungen)
- Geschaeftspartner und Kliniken (ATOS, Helios, Hafenklinik, Elbklinik etc.)
- Bewerbungen (ueber Stepstone, Indeed etc.)
- Rechnungen und Finanzen
- Interne Kommunikation
- Qodia-bezogene Themen (Investoren, Vertraege)
- Verbaende und Politik (BAG, KV, Hernienmissionen)
- Persoenliches

Jede Mail erfordert mehrere Entscheidungen: Lesen, verstehen, priorisieren, antworten, ablegen, Anhaenge speichern, Aufgaben ableiten. Das kostet Ole mehrere Stunden taeglich.

### Oles Profil
- BWLer, kein Entwickler, aber technikaffin (Selbsteinschaetzung 6-7/10)
- Motiviert, ambitioniert, strategisch denkend
- Will Dinge schnell umsetzen
- Eigene Erkenntnis: Verbeisst sich manchmal zu lang in Themen
- Will aktiv gefordert und gechallenged werden, nicht nur bestaetigt
- Braucht klare Anweisungen ohne Fachjargon

### Das uebergeordnete Ziel
E-Mail-Automatisierung ist **Schritt 1** eines groesseren Plans: Ole will langfristig seinen gesamten Arbeitsalltag automatisieren. Spaeter sollen Kalender, Dokumente, Aufgaben, Buchhaltung und mehr folgen.

---

## 2. ZIELSETZUNG: Was soll der Assistent koennen?

### Kurzfristig (jetzt)
Die KI macht Vorschlaege, Ole bestaetigt oder korrigiert:
- Mail oeffnen → KI analysiert automatisch
- Ordner-Vorschlag → Ole bestaetigt oder aendert → Mail wird verschoben
- Anhang-Vorschlag → KI schlaegt Dateiname + OneDrive-Ordner vor → Ole bestaetigt → Anhang wird abgelegt
- Antwort-Vorschlag → KI formuliert in Oles Stil → Ole bearbeitet → Senden
- Aufgaben werden extrahiert
- "Alles bestaetigen & ausfuehren" → Ein Klick erledigt alles

### Mittelfristig (Wochen/Monate)
Die KI lernt und wird besser:
- Ordner-Zuordnung wird genauer durch Feedback
- Antwort-Stil wird authentischer durch Beispiele
- KI kennt wichtige Kontakte und deren Kontext
- KI erkennt wiederkehrende Mails und handelt automatisch
- Weniger Korrekturen noetig

### Langfristig (6-12 Monate)
Die KI wird zum strategischen Berater:
- Handelt bei Routine-Mails autonom (Rechnungen ablegen, Newsletter archivieren)
- Challenged Ole bei Entscheidungen ("Du hast letzte Woche X gesagt, jetzt machst du das Gegenteil")
- Erkennt Muster in Oles Verhalten (z.B. "Du verbeisst dich gerade wieder in ein Thema")
- Kennt Oles Ziele und gleicht Handlungen damit ab
- Wird schrittweise mehr Verantwortung uebernehmen

---

## 3. VORGEHENSWEISE: Strategie & Vorgehen

### Iterativer Ansatz
Wir bauen in kleinen Schritten und testen sofort. Kein perfektes System von Anfang an – stattdessen eine Version die "gut genug" ist und die Ole ab sofort benutzt. Verbesserungen kommen beim Benutzen.

### Warum Outlook Add-in?
**Chronologie der Entscheidungen:**
1. Zuerst wurde eine eigene Web-App gebaut (index.html auf Netlify, dann localhost)
2. Die Web-App versuchte Outlook komplett nachzubauen (Ordner, Mailliste, Mail-Anzeige, Navigation)
3. Das scheiterte an einem Microsoft Graph API Bug (childFolders-Endpoint gibt fuer den Posteingang leere Ergebnisse zurueck – bestaetigt im Graph Explorer)
4. Erkenntnis: Wir bauen einen E-Mail-Client nach – das ist das falsche Ziel
5. Strategiewechsel (25.03.2026): Outlook Add-in

**Vorteile des Add-in-Ansatzes:**
- Ole bleibt in Outlook (das er eh nutzt)
- Outlook kuemmert sich um Ordner, Mails, Navigation, Suche
- Wir bauen NUR die KI-Seite: Analyse, Antwort, Ablage, Feedback
- Kein Ordner-Listing-Bug (Outlook zeigt die Ordner selbst)
- Kein eigener E-Mail-Client noetig

**Nachteile/Risiken:**
- Selbstsigniertes Zertifikat = fragil (kann nach Windows-Updates brechen)
- Server muss laufen (start-addin.bat)
- Bei Rechnerwechsel: Zertifikat, Python, Server neu einrichten

### Verworfene Alternativen
- **n8n/Make.com/Power Automate**: Verworfen weil weniger Kontrolle und weniger interaktiv
- **Netlify-Deployment**: Verworfen zugunsten von localhost (Sicherheit, Einfachheit)
- **Eigene Web-App**: Verworfen weil zu viel Outlook-Nachbau noetig (Ordner, Mails etc.)
- **Fertige AI-Mail-Add-ins** (Copilot, Mailbutler etc.): Geprueft, keines bietet die spezifischen Features (OneDrive-Ablage mit Namensformat, Lern-System, Stil-Training)

### Hybrid-Ansatz fuer spaeter (Phase 2)
Power Automate koennte spaeter fuer Routine-Mails im Hintergrund laufen (Rechnungen automatisch ablegen, Newsletter archivieren). Das Add-in bleibt fuer Mails die Oles Aufmerksamkeit brauchen.

---

## 4. ARCHITEKTUR-ENTSCHEIDUNGEN

### Tech Stack
- **Outlook Add-in** mit manifest.xml (Sideloading, kein App Store)
- **Eine einzige taskpane.html** (HTML + CSS + JS in einer Datei)
- **Python HTTPS-Server** (server.py, Port 3000, selbstsigniertes Zertifikat)
- **Office.js** fuer Outlook-Integration (CDN, eine Script-Zeile)
- **Claude API** direkt aus dem Browser (mit anthropic-dangerous-direct-browser-access Header)
- **Microsoft Graph API** fuer Aktionen (Mail verschieben, OneDrive upload, Mail senden)
- **localStorage** fuer Einstellungen und Feedback-Log
- **Lokale Textdateien** (/gedaechtnis/) als KI-Wissensbasis

### Warum diese Entscheidungen?
- **Eine Datei**: Einfach zu verstehen, einfach zu warten, kein Build-System noetig
- **Python-Server**: Python ist auf Oles Rechner installiert, kein npm/node noetig
- **Kein Framework** (React, Vue etc.): Unnoetige Komplexitaet fuer eine Seitenleiste
- **Claude API direkt im Browser**: Kein eigener Backend-Server noetig. Risiko (Key im Browser) ist akzeptiert fuer Einzelnutzer-Setup
- **Lokale Textdateien statt Datenbank**: Portabel, lesbar, versionierbar, nicht an einen Anbieter gebunden

### Azure App-Registrierung
- App: "KI Mail Assistent EHC"
- Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Redirect URIs (SPA): http://localhost:8080, https://localhost:3000
- Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite
- Hinweis: Es gibt eine zweite App-Registrierung (3c2a9a38-...) die versehentlich erstellt wurde – kann geloescht werden

---

## 5. KI-KONZEPT: Gedaechtnis & Lernen

### Grundprinzip
Claude "lernt" nicht im klassischen Sinne (keine Gewichts-Aenderung). Stattdessen:
- Wir bauen ein **strukturiertes Gedaechtnis** aus Textdateien
- Bei jeder Mail-Analyse werden relevante Gedaechtnis-Dateien als Kontext mitgeschickt
- Je besser das Gedaechtnis, desto "schlauer" wirkt die KI
- Nicht die KI wird klüger, sondern **die Akte ueber Ole wird besser**

### Gedaechtnis-Struktur
```
/gedaechtnis/
├── _config.json              ← Welche Kategorien gibt es, was wird geladen
├── profil/
│   ├── grundprofil.md        ← Wer ist Ole, Rollen, Ziele, Arbeitsweise
│   ├── kommunikationsstil.md ← (noch zu erstellen) Wie Ole schreibt
│   ├── entscheidungsmuster.md← (noch zu erstellen) Wie Ole priorisiert
│   └── psychologisches_profil.md ← (spaeter) Staerken, Schwaechen, Tendenzen
├── regeln/
│   ├── ordner.json           ← Outlook-Ordner + Zuordnungsregeln
│   ├── anhaenge.json         ← OneDrive-Ordner + Dateinamen-Regeln
│   └── antworten.json        ← Antwort-Stil, Grussformeln, Tonfall
├── kontakte/                 ← (noch zu befuellen) Bekannte Absender + Kontext
├── beispiele/
│   ├── meine_antworten/      ← (noch zu befuellen) Echte Mails von Ole als Referenz
│   └── korrekturen/          ← (noch zu befuellen) Was KI falsch machte
└── feedback/
    ├── feedback_log.json     ← (in localStorage) Chronologisches Feedback
    └── zusammenfassung.md    ← Verdichtete Erkenntnisse (wird regelmaessig aktualisiert)
```

### Drei Ebenen des Lernens

**Ebene 1: Muster-Erkennung (sofort, ab ~20 Mails)**
- Mail von ATOS → Ordner "Firmen & Organisationen / ATOS"
- Rechnung als Anhang → OneDrive/EHC/Eingangsrechnungen
- Stepstone-Mail → "Nice to have", keine Antwort noetig
- Funktioniert ueber Regeln in ordner.json die durch Feedback verfeinert werden

**Ebene 2: Stil & Kommunikation (Wochen, ab ~30 Beispiel-Mails)**
- Wie Ole Mails formuliert (Tonfall, Laenge, Grussformeln)
- Wann formal vs. informell
- Welche Formulierungen typisch sind
- Funktioniert ueber Beispiel-Mails in /beispiele/meine_antworten/

**Ebene 3: Strategischer Berater (Monate)**
- Erkennt Muster in Oles Verhalten
- Hinterfragt Entscheidungen
- Kennt Oles Ziele und gleicht Handlungen ab
- Funktioniert ueber wachsendes Profil in /profil/

### Feedback-System (zwei Quellen)
1. **Explizites Feedback**: "Alles 100% korrekt" oder "Nicht korrekt" + Freitext
2. **Implizites Feedback**: Wenn Ole den Ordner aendert, die Prio korrigiert oder die Antwort umschreibt – das wird als Korrektur gespeichert

### Portabilitaet & Sicherheit
- Alle Daten liegen lokal auf Oles Rechner
- Alles sind einfache Textdateien (JSON, Markdown)
- Wenn Ole den KI-Anbieter wechselt (z.B. von Anthropic zu OpenAI), nimmt er den /gedaechtnis/-Ordner mit
- Kann in Git versioniert werden (Entwicklung des Wissens nachvollziehbar)
- Keine Cloud-Abhaengigkeit fuer das Gedaechtnis

### Skalierung: Wann brauchen wir RAG?
- Aktuell: Gedaechtnis passt komplett in Claudes Kontext-Fenster (~20-30 Seiten Text). Kein RAG noetig.
- Spaeter: Wenn das Gedaechtnis auf hunderte Seiten waechst (z.B. Kalender, Projekte, Buchhaltung), wird RAG noetig.
- RAG = Retrieval Augmented Generation: KI durchsucht erst die Wissensbasis, liest nur relevante Teile.
- Die Struktur (Ordner = Kategorien, Dateien = Wissen) ist bereits RAG-kompatibel angelegt.

---

## 6. OLES KOMMUNIKATIONSSTIL

### Was wir bisher wissen
- Sprache: Deutsch
- Tonfall: Professionell aber nicht steif, direkt, effizient
- Laenge: So kurz wie moeglich, so lang wie noetig
- Grussformeln: Noch zu erfassen aus echten Mails
- Signatur:
  ```
  Ole Reinpold
  Geschaeftsleitung
  M +49 151 1531 1887
  E o.reinpold@hernie.de
  Website | LinkedIn

  HAMBURGER HERNIEN CENTRUM
  Elbe Hernien Centrum EHC GmbH | Wendenweg 12 | 21465 Wentorf
  Geschaeftsfuehrer: Dr. med. Wolfgang Reinpold
  Amtsgericht Luebeck, HRB 20507 HL
  ```

### Was noch erfasst werden muss
- Echte Beispiel-Mails von Ole sammeln (die ersten 10-20 Antworten)
- Grussformeln analysieren (Wann "Sehr geehrter", wann "Hallo", wann "Hi"?)
- Typische Formulierungen identifizieren
- Unterschied zwischen EHC-Mails und Qodia-Mails im Stil

### Wie der Stil gelernt wird
1. Ole schreibt/korrigiert Antworten im Add-in
2. Die korrigierten Antworten werden als Beispiele gespeichert
3. Bei neuen Mails werden aehnliche Beispiele als Referenz mitgeschickt
4. Ueber Zeit wird der generierte Stil immer authentischer

---

## 7. PRIORITAETEN (von Ole festgelegt)

### EXTREM WICHTIG
1. **Anhaenge in OneDrive ablegen** mit Format JJMMTT_Organisation_Dateiname.ext
   - Beispiel: 260325_ATOS_Klinik_Rechnung_2026-0342.pdf
   - KI schlaegt Name + Zielordner vor, Ole bestaetigt
   - OneDrive-Ordner: EHC (Eingangsrechnungen, Vertraege, Korrespondenz, Personal, Finanzen, OP-Dokumentation), Qodia (Allgemein, Investoren, Vertraege), Privat (Allgemein)

2. **Lern-System aus Feedback**
   - KI wird mit jeder bearbeiteten Mail besser
   - Explizites + implizites Feedback
   - Wissen bleibt bei Ole (lokal, portabel)

3. **Antworten in Oles Stil formulieren**
   - Authentisch, nicht generisch
   - Trainiert aus echten Beispielen
   - Bearbeitbar vor dem Senden

### WICHTIG
4. Ordner-Empfehlung + Mail verschieben
5. Aufgaben-Extraktion (max 3, nie kleinteilig, nie "Beleg ablegen")

### WENIGER WICHTIG
6. Prioritaetsstufen (Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten)

### UI-Regeln
- keine_antwort_noetig: true bei Rechnungen, Newslettern, Infomails
- Antwort als Toggle (Ja/Nein), nicht als Button
- KI-Analyse standardmaessig zugeklappt
- Aufgaben: nie kleinteilig, nie Ablage-Aufgaben wenn Anhang eh abgelegt wird

---

## 8. VISION: Roadmap

### Phase 1: Basis (diese Woche)
- Add-in analysiert Mails und macht Vorschlaege
- Ole bestaetigt/korrigiert alles manuell
- Feedback wird gespeichert
- Anhaenge koennen in OneDrive abgelegt werden

### Phase 2: Lernen (naechste Wochen)
- Ordner-Zuordnung wird durch Feedback genauer
- Antwort-Stil wird aus Beispielen trainiert
- Kontakt-Datenbank waechst
- Wiederkehrende Mails werden erkannt

### Phase 3: Teilautonomie (1-3 Monate)
- Routine-Mails (Rechnungen, Newsletter) werden automatisch verarbeitet
- KI braucht bei 50%+ der Mails keine Korrektur mehr
- Evtl. Power Automate fuer Hintergrund-Verarbeitung
- KI beginnt Ole zu challengen

### Phase 4: Erweiterung (3-6 Monate)
- Kalender-Integration
- Aufgaben-Management
- Weitere Automatisierung des Arbeitsalltags

### Phase 5: Strategischer Berater (6-12 Monate)
- KI kennt Oles Ziele, Muster und Tendenzen
- Proaktive Hinweise ("Du verbeisst dich gerade wieder")
- Strategische Empfehlungen basierend auf angesammeltem Wissen
- KI handelt bei Routine weitgehend autonom

---

## Zusammenarbeit zwischen Ole und Claude

### Oles Rolle
- Definiert was er braucht (Sparringspartner)
- Testet und gibt Feedback
- Trifft strategische Entscheidungen
- Macht Azure/Microsoft-Konfiguration selbst
- Traegt API-Keys und Credentials selbst ein

### Claudes Rolle (Claude Code)
- Sparringspartner: Challenget Ole, hinterfragt Entscheidungen, weist auf Risiken hin
- Umsetzer: Schreibt Code, loest technische Probleme
- Dokumentiert: Haelt alles in CLAUDE.md, PROJEKTSTAND.md, KONZEPT.md fest
- Aktualisiert am Ende jeder Session alle relevanten Dateien

### Wichtige Arbeitsregeln
- Alles in einfacher Sprache erklaeren (Ole ist kein Entwickler)
- ALLE Ergebnisse in Dateien sichern, NIE nur im Chat-Kontext lassen
- Bei jedem Chatwechsel: Dateien aktualisieren
- Lieber zu viel dokumentieren als zu wenig
- "Stopp" heisst sofort aufhoeren
- Keine stillen Annahmen – lieber einmal zu viel fragen
