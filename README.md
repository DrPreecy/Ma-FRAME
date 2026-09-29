# Ma-FRAME

Ma-FRAME ist ein nutzergeführtes Denk- und Operator-System, das persönliche Ideen bewahrt und Menschen vom ungeordneten inneren Kontext über Erkundung und Planung bis zur Produktion und zum Lernen aus realer Nutzung begleitet. Es soll weder ein starres Unternehmens-Framework noch ein bloßes Eingabeformular sein: Die Struktur übernimmt Dokumentations- und Orientierungsarbeit, während die Person Richtung, Bedeutung und Entscheidungen verantwortet.

Diese Arbeitsumgebung bildet den in den Quelldokumenten beschriebenen Entwicklungsweg ab. Die Phasenbezeichnungen folgen dem ITP; eine Phase ist nicht automatisch gleich gut ausgearbeitet oder empirisch bestätigt.

## Entwicklungsweg des Frameworks

| Phase | Name aus dem ITP | Arbeitsbereich |
| --- | --- | --- |
| I | Ideen Entwerfung | [`docs/10_framework/01_ideen-entwerfung/`](docs/10_framework/01_ideen-entwerfung/) |
| II | Ideen Entwicklung | [`docs/10_framework/02_ideen-entwicklung/`](docs/10_framework/02_ideen-entwicklung/) |
| III | Idee zu Produktion | [`docs/10_framework/03_idee-zu-produktion/`](docs/10_framework/03_idee-zu-produktion/) |
| IV | Produktion | [`docs/10_framework/04_produktion/`](docs/10_framework/04_produktion/) |
| V | Launch / After Launch | [`docs/10_framework/05_launch-after-launch/`](docs/10_framework/05_launch-after-launch/) |
| VI | Execution Regeln | [`docs/10_framework/06_execution-regeln/`](docs/10_framework/06_execution-regeln/) |
| VII | Systemübergreifende Framework-Logik & Philosophie | [`docs/10_framework/07_systemlogik-philosophie/`](docs/10_framework/07_systemlogik-philosophie/) |

Die Struktur unterscheidet außerdem **Arbeitsartefakte** von **Framework-Phasen**: `00_quellen` bewahrt und analysiert das Ausgangsmaterial; `10_framework` enthält die Spezifikation nach Phase I–VII; `20_entscheidungen`, `30_arbeitsstand` und `40_vorlagen` dokumentieren, steuern und unterstützen die iterative Arbeit. Diese Arbeitsbereiche sind keine zusätzlichen Framework-Phasen.

## Stand und nächster Schritt

Der Autorenbericht und der KI-Tätigkeitsbericht benennen den dort dokumentierten Durchlauf von Schritt I.1, **Offload your Context**, als abgeschlossen und Schritt I.2, **Guided thought extracting**, als nächsten Schritt. Die Spezifikation von I.1 ist als wiederholbarer Erfassungs- und Übergabeprozess stabilisiert. Beides besagt weder, dass Phase I oder das Ideen-Produktprofil abgeschlossen sind, noch bestätigt es die Wirksamkeit des Modells. Das ITP skizziert darüber hinaus bereits die Phasen II–VII, weist aber selbst auf fehlenden Realitätsabgleich hin.

Der konkrete Arbeitsstand und die nächsten Einzelsitzungen stehen in [`docs/30_arbeitsstand/ROADMAP.md`](docs/30_arbeitsstand/ROADMAP.md). Belege, Ableitungen und Widersprüche sind in [`docs/00_quellen/QUELLENANALYSE.md`](docs/00_quellen/QUELLENANALYSE.md) festgehalten; ungeklärte Punkte erhalten IDs in [`docs/30_arbeitsstand/OFFENE_FRAGEN.md`](docs/30_arbeitsstand/OFFENE_FRAGEN.md).

## Im Repository arbeiten

1. Quelldokumente unverändert lassen; neue Fassungen nur als nachvollziehbare Extraktion ergänzen.
2. Für eine Framework-Änderung Phase und betroffenen Baustein benennen, den Baustein-Entwurf anpassen und offene Fragen aktualisieren.
3. Änderungen als Pull Request mit der Vorlage [`.github/pull_request_template.md`](.github/pull_request_template.md) einreichen und das zugehörige Review-Gate dokumentieren.
4. Lokal `make check` ausführen. Neue `.docx`-Quellen können mit `make extract` nach Markdown extrahiert werden.

Arbeitsregeln und Definition of Done: [`CONTRIBUTING.md`](CONTRIBUTING.md).
