# KI Mail Assistent – Projektstand (25.03.2026)

## Wichtig: Kein Gedaechtnis zwischen Chats
Jeden neuen Chat starten mit:
"Lies https://raw.githubusercontent.com/olereinpold92/ki-mail-assistent/main/PROJEKTSTAND.md und mach weiter."
Alle Entscheidungen hier dokumentieren damit sie nicht nochmal diskutiert werden muessen.

## Wer ist Ole?
- Ole Reinpold, Ansprache: Du, Sprache: Deutsch
- Prokurist/GF: Elbe Hernien Centrum EHC GmbH (Hamburger Hernien Centrum), 2 Standorte Hamburg, ~8 Mitarbeiter, Hernienchirurgie
- Mitgruender/GF: Qodia GmbH (KI-Loesungen GOAe-Abrechnung), 4 Gruender
- E-Mail: o.reinpold@hernie.de (Microsoft 365 Business Standard)
- Kein Entwickler, Technikaffinitaet 6-7/10.
- Will direkte Anleitungen, nicht durch UI navigiert werden.
- Will als Sparringspartner gefordert werden, nicht nur bestaetigt.

## Zusammenarbeit-Regeln (IMMER beachten)
- Ole navigiert den Browser IMMER selbst. Claude oeffnet KEINE Tabs, navigiert KEINE URLs, klickt NICHTS im Browser - ausser Ole sagt explizit "mach das fuer mich".
- Claude gibt klare Schritt-fuer-Schritt-Anweisungen wenn Ole etwas selbst machen soll.
- Kein Fachjargon ohne Erklaerung.
- Claude uebernimmt: Code schreiben, GitHub API pushes, komplexe Konfigurationen.
- Ole uebernimmt: Einfache Klicks, Seiten aufrufen, Credentials eingeben, testen.
- Immer erst Preview zeigen bevor deployed wird.

## Chat-Prozess
- Ein Chat = ein sinnvolles Aufgabenpaket. Wenn ein Chat zu lang wird, neuen starten.
- Neuer Chat startet immer mit: "Lies PROJEKTSTAND.md..."
- Am Ende jedes Chats: PROJEKTSTAND.md aktualisieren mit allem was geaendert/entschieden wurde.
- Netlify Build-Credits: Sparsam einsetzen. Maximal 1-2 Deploys pro Session. Nie fuer kleine Fixes deployen.

## Warum dieser KI Mail Assistent?
Ole bearbeitet taeglich viele E-Mails als GF von EHC und Qodia. Das kostet zu viel Zeit.
Ziel: Interface oeffnen, alle neuen Mails sehen, KI-Analyse lesen, mit einem Klick abarbeiten.
Langfristig: KI handelt autonom. Kurzfristig: KI macht Vorschlaege, Ole bestaetigt.
E-Mail ist Schritt 1. Spaeter: Kalender, Dokumente, Aufgaben, Buchhaltung etc.

## Was der Assistent koennen soll (pro Mail)
1. Prioritaet vorschlagen: Wichtig & Dringend / Wichtig / Muss gemacht werden / Nice to have / Nachhalten
2. Antwortvorschlag generieren (in Oles Stil, auf Deutsch, bearbeitbar)
3. E-Mail-Ordner vorschlagen (wo die Mail in Outlook abgelegt werden soll)
4. Anhaenge in OneDrive ablegen mit Dateiname: JJMMTT_Organisation_Dateiname.ext
5. Aufgabenliste: Nur was UEBER Antworten+Ablegen hinausgeht. Nicht kleinteilig. Keine Ablage-Aufgaben. Max 3.
6. Feedback-System: "Alles 100% korrekt" oder "Nicht korrekt" + Freitext. KI lernt daraus UND aus manuellen Anpassungen.

## KI-Prompt-Regeln (entschieden)
- Aufgaben: Nur was UEBER Antworten+Ablegen hinausgeht, keine Teilschritte, keine Ablage-Aufgaben
- keine_antwort_noetig: true bei Rechnungen, Newslettern, Infomails
- KI lernt aus Korrekturen via localStorage

## Tech Stack & Infrastruktur
- Alles in einer index.html (kein separates app.js - wurden zusammengefuehrt)
- GitHub Repo: olereinpold92/ki-mail-assistent (Token in 1Password, kein Ablauf)
- Netlify: https://bright-cannoli-eeaa45.netlify.app / Login: EHC2026
- Netlify Plan: Pro ($9/Monat, 1000 Build-Credits/Monat)
- Auto-Deploy: war aktiv, sollte DEAKTIVIERT sein nach jedem Deploy
- Azure Client ID: aa8510ea-c13b-4c87-bb7d-3bde7bf6b2f0
- Azure Tenant ID: 710620de-9a6b-4cca-bf53-99ce2a3e407f
- Azure Redirect URI: https://bright-cannoli-eeaa45.netlify.app/ (SPA)
- Azure Berechtigungen: User.Read, Mail.ReadWrite, Mail.Send, Files.ReadWrite + Adminzustimmung erteilt
- Azure Auth: Impliziter Grant (Zugriffstoken + ID-Token) aktiviert

## Deploy-Workflow (EINZIGER funktionierender Weg)
1. Claude erstellt index.html und stellt sie als Download bereit (present_files Tool)
2. Ole laedt die Datei herunter
3. github.com/olereinpold92/ki-mail-assistent -> "Add file" -> "Upload files"
4. Datei als index.html hochladen -> Commit changes
5. In Netlify: Deploys -> "Trigger deploy" manuell ausloesen
6. Danach: Auto-Deploy sofort wieder deaktivieren

NIEMALS versuchen:
- outerHTML pushen (erzeugt kaputte Datei - war der Fehler am 24.03.)
- Datei in Chunks via JavaScript uebertragen (zu langsam/fehleranfaellig)
- Datei-Dialog automatisch oeffnen (Browser-Sicherheitssperre)
- Claude navigiert Browser selbst fuer Deploys

## Entschiedene Punkte - NICHT nochmal diskutieren
- Claude Code: ABGELEHNT. Ole ist kein Entwickler.
- n8n/Make.com/Power Automate als Basis: VERWORFEN. Direkte Graph API im Interface ist besser.
- Ein-Datei-Ansatz (alles in index.html): BEIBEHALTEN, kein separates app.js
- App-Passwort: EHC2026
- Hoster: Netlify Pro
- Microsoft 365 als Mail-Hub fuer EHC: ENTSCHIEDEN und implementiert
- Architektur (GitHub + Netlify + Graph API + Claude API direkt im Browser): BESTAETIGT als richtig
- Sicherheit (Claude API Key im localStorage): akzeptiertes Risiko fuer Einzelnutzer, spaeter Backend

## Was in der aktuellen index.html fertig ist (Stand 25.03.2026)

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

## Microsoft 365 Setup (EHC)
- Postfach: o.reinpold@hernie.de auf Microsoft 365 Business Standard
- MX-Record bleibt bei all-inkl (Mitarbeiter unberuehrt)
- Weiterleitung: all-inkl -> Microsoft 365 als Kopieempfaenger
- SPF: v=spf1 a mx include:spf.kasserver.com include:spf.protection.outlook.com ~all
- Internal Relay konfiguriert (hernie.de nicht autoritaetiv in Exchange)
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

## Was heute (25.03.2026) noch zu tun ist
- preview6.html (das fertige UI mit allen 17 Features) wurde noch nicht korrekt deployed
- Aktuell laeuft noch der alte Stand auf Netlify
- Naechste Aufgabe: index.html mit dem fertigen Stand deployen
- Danach: echte Tests mit Microsoft-Verbindung