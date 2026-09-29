# Agenten-Übergabe

Diese Vorlage trennt konzeptionelle Prüfung und Ausführung. Ein
theorieorientierter Agent begründet zuerst den kleinsten sinnvollen Auftrag.
Ein ausführender Coding-Agent erhält danach einen eindeutigen Arbeitsauftrag,
ohne offene Grundsatzentscheidungen selbst zu treffen.

## Einordnung

- **Arbeitspaket:** `WP-…`
- **Phase / Baustein:**
- **Gewünschtes Ergebnis:**
- **Verantwortliche menschliche Freigabe:**

## Theorie-Review

- **Ausgangslage:** aktueller Stand und konkrete Belege mit Dateipfaden
- **Befunde:** Fehler, Logiklücken, ungenutzte Möglichkeiten und Risiken nach
  Priorität
- **Entscheidung:** gewählte Lösung und verworfene Alternativen
- **Offene Fragen:** betroffene OF-IDs; nicht entschiedene Punkte

## Ausführungsauftrag

- **Ziel:** ein beobachtbares Ergebnis
- **Erlaubte Dateien:** abschließende Liste
- **Nicht verändern:** Quellen, angrenzende Bausteine und weitere Grenzen
- **Arbeitsschritte:** kurze, vollständig ausführbare Reihenfolge
- **Nicht-Ziele:** ausdrücklich ausgeschlossene Verbesserungen

## Abnahme

- **Akzeptanzkriterien:** konkrete, prüfbare Bedingungen
- **Prüfbefehle:** mindestens `make check`; weitere vorhandene Prüfungen
- **Manuelle Prüfung:** erwartetes Ergebnis und Prüfschritte
- **Stopp-/Eskalationskriterien:** abbrechen und rückfragen, wenn eine
  Grundsatzentscheidung, Quellenänderung oder Scope-Erweiterung nötig wird
- **Erwartete Rückgabe:** geänderte Dateien, Prüfergebnisse und verbleibende
  Risiken
