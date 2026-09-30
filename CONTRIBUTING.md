# Mitwirken an Ma-FRAME

Diese Richtlinien halten die Arbeit quellengebunden, nutzergeführt und überprüfbar. Sie beschreiben den Repository-Workflow, nicht zusätzliche Phasen des Frameworks.

## Ablauf einer Arbeitssitzung

1. **Einordnen:** Phase I–VII und den betroffenen Baustein oder eine offene Frage bestimmen. Bei Bedarf zuerst Quelle und bisherigen Stand lesen.
2. **Ziel setzen:** Ein beobachtbares Ergebnis für diese Sitzung festlegen; offene konzeptionelle Entscheidungen als Frage dokumentieren statt sie stillschweigend zu entscheiden.
3. **Bearbeiten:** Änderungen additiv und rückverfolgbar formulieren. Originalbegriffe und Nutzerintention bewahren; Interpretation als solche markieren.
4. **Abgleichen:** Schutzregeln, Abgrenzungen, Beispiele und Abhängigkeiten betroffener Bausteine prüfen. Neue oder geschlossene Fragen im Fragen-Backlog nachführen.
5. **Prüfen und sichern:** `make check` ausführen, den Pull-Request-Umfang prüfen und den Stand als Änderung nachvollziehbar sichern.

Bei agentengestützter Arbeit erstellt ein theorieorientierter Agent zuerst eine
geschlossene [`Agenten-Übergabe`](docs/40_vorlagen/agenten-uebergabe.md). Der
ausführende Agent setzt nur diesen Auftrag um und eskaliert bei den dort
festgelegten Stoppkriterien.

## Definition of Done

- Phase, Baustein und gewünschtes Ergebnis sind im PR benannt.
- Jede inhaltliche Änderung ist entweder einer Quelle, einer expliziten Ableitung oder einer offenen Frage zugeordnet.
- Betroffene Bausteine enthalten Zweck, Abgrenzung, Bestandteile, Regeln, Beispiel, offene Punkte und einen gültigen Status.
- Jeder `[OFFEN: OF-nnn]`-Marker verweist auf einen Eintrag im Fragen-Backlog; erledigte Fragen sind dort mit Ergebnis und Verweis geschlossen.
- `make check` ist erfolgreich oder die Abweichung ist begründet und sichtbar.
- Keine Quelle wurde stillschweigend überschrieben oder gekürzt.

## Benennung und Status

- Phasenbezeichnungen folgen dem ITP: `Ideen Entwerfung`, `Ideen Entwicklung`, `Idee zu Produktion`, `Produktion`, `Launch / After Launch`, `Execution Regeln` und `Systemübergreifende Framework-Logik & Philosophie`.
- Dateien und Ordner verwenden kleingeschriebene, deutschsprachige, mit Bindestrichen getrennte Namen.
- Statuswerte sind `Entwurf`, `In Arbeit` oder `Stabil`. `Stabil` bedeutet einen geprüften Dokumentationsstand, nicht empirischen Wirksamkeitsnachweis.
- Fragen erhalten fortlaufende IDs `OF-001`, `OF-002`, …; vorhandene IDs werden nicht wiederverwendet.
- Entscheidungen werden als `NNNN-kurzer-titel.md` dokumentiert. Sie halten Kontext, Entscheidung und Folgen fest.

## Issues, Labels und Reviews

Für GitHub-Issues sind Labels wie `stufe:1`, `stufe:2` bis `stufe:7`, `baustein`, `offene-frage` und `review` vorgesehen. Die Phasenangabe bezeichnet die ITP-Phase, kein Repository-Meilenstein. Ein Issue sollte genau eine Hauptphase enthalten; abhängige Phasen können im Text genannt werden.

Ein Review prüft insbesondere Quellentreue, Nutzerhoheit, Zeitpunkt von Messbarkeit/Kritik, Rückverfolgbarkeit des inneren Inputs sowie Auswirkungen auf verbundene Räume. Reviewer sollen Fragen sichtbar machen, nicht ungeklärte Grundsatzentscheidungen stellvertretend treffen.
