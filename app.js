// ── CONFIG ──
var PW = 'EHC2026';
var CLAUDE_KEY = ''; // Wird aus localStorage geladen
var CLIENT_ID = ''; // Azure App Client ID
var TENANT_ID = 'common'; // oder spezifische Tenant ID

var F = ['EHC / Eingangsrechnungen','EHC / Vertraege','EHC / Korrespondenz','EHC / Personal','EHC / Finanzen','EHC / OP-Dokumentation','Qodia / Allgemein','Qodia / Investoren','Qodia / Vertraege','Privat / Allgemein','Kein Anhang'];

// ── STATE ──
var M = []; // Wird aus Graph API befüllt
var sel = null;
var accessToken = null;
var isLoadingAI = false;