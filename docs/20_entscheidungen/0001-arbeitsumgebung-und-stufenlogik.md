# ADR-0001: Arbeitsumgebung und Stufenlogik

- Status: Angenommen
- Datum: 2026-09-29
- Phase/Baustein: Repository-Arbeitsweise; Phasen I–VII
- Beteiligte: Repository-Ersteinrichtung

## Kontext

Das Repository enthielt drei unveränderte DOCX-Quelldokumente und eine README ohne Inhalt außer dem Titel. Die Quellen benennen einen mehrstufigen Framework-Ablauf und beschreiben I.1 als abgeschlossen, während I.2 der nächste Schritt ist. Ein Arbeitsbereich muss den Framework-Ablauf widerspiegeln, ohne Verwaltungsmaterial als zusätzliche Framework-Phasen auszugeben.

## Entscheidung

Die Quellen werden in `docs/00_quellen/` extrahiert und analysiert. Die lebende Spezifikation liegt in `docs/10_framework/` mit einem eigenen Phasenordner für jede ITP-Phase I–VII. Entscheidungen, Arbeitsstand und Vorlagen liegen getrennt in `docs/20_entscheidungen/`, `docs/30_arbeitsstand/` und `docs/40_vorlagen/`; README und Contribution Guide erklären, dass dies Repository-Artefakte und keine zusätzlichen Framework-Phasen sind.

Phasenbezeichnungen folgen der ITP-Fassung. Phase VI und VII werden vorerst als nummerierte Querschnittsphasen beibehalten, bis ihre Einordnung geklärt ist. Der Arbeitsstand nennt den dokumentierten Durchlauf von Schritt I.1 „Offload your Context“ abgeschlossen und I.2 „Guided thought extracting“ als nächsten Schritt.

## Erwogene Optionen

- Generische Softwarestruktur ohne Abbildung des Phasenmodells: verworfen, da sie die konzeptionelle Arbeitsweise verdecken würde.
- Verwaltungsthemen als zusätzliche Phasen behandeln: verworfen, da sie keine Framework-Phasen sind.
- Phasen VI und VII stillschweigend zu Leitprinzipien umbenennen: verworfen, da die Quellen sie nummerieren und ihre Einordnung nicht abschließend klären.

## Folgen

Der Aufbau ist quellengetreu auffindbar und kann mit zunehmender Klärung weiterentwickelt werden. Die Benennung und die ITP-Phasenlogik sind noch keine Bestätigung ihrer Wirksamkeit. Die offene Einordnung von VI/VII wird als OF-009 nachgeführt.

## Quellen und Rückverfolgbarkeit

- `docs/00_quellen/QUELLENANALYSE.md`
- `docs/30_arbeitsstand/OFFENE_FRAGEN.md` – OF-009, OF-012
