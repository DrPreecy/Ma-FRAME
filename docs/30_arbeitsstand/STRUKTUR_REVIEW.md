# Kritischer Repository-Struktur-Review

Stand: 2026-09-29

## Auftrag und Methode

Geprüft wurden Auffindbarkeit, Quellentreue, Arbeitsfluss und automatische
Absicherung der Repository-Struktur. Grundlage waren die dokumentierte
Strukturentscheidung
[`ADR-0001`](../20_entscheidungen/0001-arbeitsumgebung-und-stufenlogik.md),
der [Beitragsablauf](../../CONTRIBUTING.md), die
[Roadmap](ROADMAP.md) sowie der bisherige Validator
`tools/check_framework.py`. Quelleninhalte wurden nicht neu entschieden.

## Was bereits trägt

- Die sieben ITP-Phasen sind von Quellen, Entscheidungen, Arbeitsstand und
  Vorlagen getrennt. Verwaltungsmaterial wird nicht als zusätzliche Phase
  ausgegeben.
- Quellen, Synthese, offene Fragen und Entscheidungen haben eigene,
  nachvollziehbare Ablageorte.
- Baustein- und Review-Vorlagen sowie `make check` machen den vorgesehenen
  Arbeitsablauf grundsätzlich ausführbar.
- Die Roadmap zerlegt die weitere Framework-Entwicklung in kleine
  Arbeitspakete mit überprüfbaren Ergebnissen.

## Priorisierte Befunde

| Priorität | Befund und Beleg | Behandlung |
| --- | --- | --- |
| P0 | Der bisherige Validator suchte beliebige Ordner nach dem Muster `[0-9][0-9]_*`. Eine isolierte Probe mit nur einem frei benannten Phasenordner und einem Baustein bestand deshalb erfolgreich. Die in ADR-0001 festgelegten Phasen I–VII waren nicht gegen Löschen, Umbenennen oder Ergänzen geschützt. | `tools/check_framework.py` prüft nun die sieben exakten Ordner, mindestens einen Baustein je Phase, unerwartete Phasenordner und zentrale Arbeitsdateien. Regressionstests sichern diese Regeln. |
| P1 | Der Beitragsablauf verlangte Einordnung und Prüfung, definierte aber keine eindeutige Grenze zwischen theoretischer Klärung und mechanischer Ausführung. Dadurch hätte ein Coding-Agent offene Grundsatzfragen stillschweigend entscheiden oder den Umfang erweitern können. | Die Vorlage [`agenten-uebergabe.md`](../40_vorlagen/agenten-uebergabe.md) trennt Theorie-Review, ausführbaren Auftrag, Nicht-Ziele, Abnahme und Eskalation. |
| P1 | Roadmap-Pakete, OF-IDs und Bausteinstatus sind nur teilweise maschinell miteinander verknüpft. Der Validator prüft OF-Marker, aber nicht, ob Statusänderungen oder erledigte Pakete vollständig in Roadmap, Backlog und Änderungsprotokoll nachgeführt wurden. | Nicht in diesem Struktur-Paket automatisieren. Zuerst anhand von WP-I-02 beobachten, welche Konsistenzregel stabil genug für CI ist. |
| P2 | Issue-Vorlagen setzen Labels wie `baustein`, `offene-frage` und `review` voraus; im Repository ist keine Label-Synchronisation definiert. Bei einem neuen oder neu konfigurierten Repository kann die vorgesehene Einordnung daher fehlen. | Vor Nutzung der Vorlagen einmalig auf GitHub prüfen. Nur bei bestätigter Lücke ein eigenes Infrastruktur-Arbeitspaket anlegen. |

## Nicht gefundene oder bewusst nicht gelöste Punkte

- Es gibt keinen belegten Grund, die bestehende Phasen- oder
  Verzeichnisstruktur erneut umzubauen.
- Die DOCX-Quellen und ihre Extraktionen sind keine ungenutzten Dubletten:
  Original und durchsuchbare Arbeitsfassung erfüllen unterschiedliche Zwecke.
- Inhaltliche Lücken des Frameworks bleiben im
  [Fragen-Backlog](OFFENE_FRAGEN.md); dieser Review entscheidet sie nicht.
- Neue Tools, Abhängigkeiten oder zusätzliche Planungssysteme sind für die
  festgestellten Strukturprobleme nicht erforderlich.

## Verbindlicher Ablauf für weitere Pakete

1. Ein theorieorientierter Agent prüft Quellen, vorhandene Entscheidungen und
   betroffene Bausteine kritisch.
2. Er füllt die
   [Agenten-Übergabe](../40_vorlagen/agenten-uebergabe.md) mit Belegen,
   Dateigrenzen, Nicht-Zielen und Akzeptanzkriterien aus.
3. Ein ausführender Coding-Agent setzt ausschließlich diesen geschlossenen
   Auftrag um und eskaliert bei einem Stoppkriterium.
4. `make check`, manuelle Abnahme und menschliche Freigabe schließen das
   Arbeitspaket ab.

Dieser Ablauf nutzt die bestehenden `WP-…`-IDs. Er führt weder ein paralleles
Backlog noch eine zusätzliche Framework-Phase ein.
