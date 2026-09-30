# Quellenanalyse

## Material und Vorgehen

Die drei ursprünglichen DOCX-Dateien liegen im Repository-Root und bleiben unverändert. Die am 29.09.2026 bereitgestellten Markdown- und PDF-Quellen liegen ebenfalls unverändert in diesem Verzeichnis. Die Markdown-Extraktionen der DOCX-Dateien dienen Suche, Zitierung und Review; sie sind keine Ersatzfassungen der formatierten Originale. Die Extraktion erhält den Text in Dokumentreihenfolge und stellt erkannte Überschriften, Absätze und Tabellen als Markdown dar. Formatierung, eingebettete Medien und mögliche Word-spezifische Semantik sind damit nicht vollständig abgebildet.

- [Autorenbericht](autorenbericht.md): subjektive Prozessdokumentation und Reflexion der Phase I.1.
- [ITP](itp.md): Beschreibung des Kernablaufs und der Phasen I–VII; ausdrücklich als Vision ohne Realitätsabgleich/Recherchen bezeichnet.
- [KI-Tätigkeitsbericht](ki-taetigkeitsbericht.md): Dokumentation der KI-Rolle und rückblickende methodische Synthese.
- [Marlons Framework, Export vom 29.09.2026](Marlons_Framework_zur_Innovationsentwicklung_2026-09-29.md): unveränderter Gesprächsexport mit Entwürfen und Gemini-Rückmeldungen; kein freigegebener Ersatz für ITP oder Framework-Spezifikation.
- [Architektonische Kartierung des Operator-Paradigmas](Architektonische.Kartierung.und.Systemumfeld.des.Operator-Paradigmas.pdf): bereitgestellter Gemini-Deep-Research-Bericht; die Einordnung und vorläufigen Antworten stehen in der [Analyse](gemini-deep-research-analyse.md).

## Was Ma-FRAME nach den Quellen ist

Ma-FRAME (im Material auch „Marlons Framework“ genannt) ist ein nutzergeführtes Denk-, Planungs- und Operator-System. Es soll eine Person – insbesondere Menschen, die intuitiv oder assoziativ denken und nicht gelernt haben, Vorhaben zu planen – vom persönlichen, ungeordneten Ausgangskontext zu einem begründbaren Konzept, einem Produktionsplan, einer tatsächlichen Umsetzung und kontrolliertem Lernen aus der Nutzung führen. Der Gegenstand kann laut ITP Software, Hardware oder ein gemischtes Vorhaben sein.

Das Problem ist nicht primär fehlende Ausführungssoftware. Die Quellen beschreiben ein „Henne-Ei-Problem“: erfolgreiche Umsetzung verlangt Planung, doch vielen Menschen fehlt ein erlerntes Planungsmodell. Starre Corporate-Frameworks und reine Ausführungstools lassen aus Sicht des Autors zu wenig geschützten Raum für individuelle Ideen; ungeführte Freiheit und KI-Prompting ohne Plan erzeugen dagegen Überforderung und Abhängigkeit. Ma-FRAME soll Orientierung und administrative Struktur bereitstellen, ohne die Person zum messbaren Ausführungsorgan zu machen.

Die KI ist dabei Resonanzraum, Protokollant, Strukturkatalysator und später Ausführungswerkzeug – nicht schöpferische Autorität. Der Mensch behält die Richtungs-, Freigabe- und Verwerfungsentscheidungen. Das Zielbild ist ein interaktives Mentorsystem, kein totes Formular.

## Phasenmodell und Entwicklungsstand

| ITP-Phase | Zweck und erkennbare Logik | Quellenstatus |
| --- | --- | --- |
| I. Ideen Entwerfung | Inneren Input unbewertet bergen; durch sokratischen Dialog vertiefen; beides in einem zunächst unverbindlichen Ideen-Produktprofil sichern. ITP-Schritte: **Offload your Context**, **Guided thought extracting**, Zusammenführung zu A. | Autorenbericht und KI-Bericht benennen I.1 als abgeschlossen; I.2 ist der nächste Schritt. ITP beschreibt I.1 und I.2. |
| II. Ideen Entwicklung | Das Profil mit Außenperspektiven erkunden, innere/äußere Differenzen untersuchen, einen Lösungsentwurf formen und das Verständnis/ die Begründbarkeit validieren: **Get Information**, **Understand the Differences**, **Form your Opinion**, **Prove your Opinion**. | Im ITP detailliert, aber nicht als empirisch validiert ausgewiesen. |
| III. Idee zu Produktion | Das validierte Konzept in einen Produktions-Blueprint überführen. Sechs vernetzte Räume: Projekt-, Produkt-, Business-, Brand-, Personalmanagement sowie Pre-Production & Workspace Setup. | ITP beschreibt Zweck, Regeln und teilweise Kriterien; der KI-Bericht bezeichnet die Räume als synthetisierte Arbeit. Abhängigkeiten und Gate-Logik bleiben teils offen. |
| IV. Produktion | Verbindliche Ausführung des in Phase III freigegebenen Blueprints; Orchestrierung etablierter Werkzeuge statt Erfindung eines neuen Code- oder Agentensystems. | ITP benennt einen harten Produktionsübergang und Ausführungsregeln. |
| V. Launch / After Launch | Release/Rollout, Monitoring sowie Rückführung realer Daten und Erfahrungen in kontrollierte Optimierungsschleifen. | Im ITP knapp beschrieben; Feedback-, Datenschutz- und Änderungsverfahren fehlen. |
| VI. Execution Regeln | Querschnittsregeln: Nutzerautorität, Reversibilität vor Produktion, keine Bewertung im Brainstorming und Ende bei erreichtem nutzerdefiniertem Fertig-Kriterium. | Vier Regeln im ITP explizit; Verhältnis zu den Gates und Phasen nicht formalisiert. |
| VII. Systemübergreifende Framework-Logik & Philosophie | Leitstrahl mit modularen, vernetzten Räumen; menschliche Orientierung zwischen Überregulierung und haltloser Freiheit; GUFP-Prinzip, Save State und dynamisches Routing. | Philosophisch ausführlich im ITP; Verhältnis zu VI und die Bedeutung einzelner Begriffe sind offen. |

Die Phasen I–V bilden überwiegend einen gerichteten Entwicklungsweg, jedoch keine starre lineare Pipeline: Phase III beschreibt vernetzte Räume und Rückkopplungen, Phase VII dynamische Schleifen. Phase VI und VII wirken eher systemübergreifend als als gleichartige Arbeitsschritte. Diese Lesart ist eine Synthese, keine endgültige Festlegung.

## Kernkonzepte und Regeln

- **Innerer Input `x`:** persönliche Vision, Wünsche und Kontext; Ursprung und Rückverfolgbarkeit sollen geschützt bleiben.
- **Äußerer Input `y`:** Recherche, Gegenhypothesen und externe Perspektiven, gezielt erst in Phase II.
- **Rückverfolgbarkeit / `x = y`:** KI-Bericht interpretiert die Gleichung als funktionale Rückverfolgbarkeit, nicht als numerische Gleichheit: Ergebnisse sollen auf ursprünglichen Input oder bewusst akzeptierte Ergänzungen zurückführbar sein.
- **GUFP:** Im ITP sowohl Akronym für „Gesunder, unvoreingenommener, freier Prozess“ als auch als Phase-II-Ablauf „Get / Understand / Form / Prove“ verwendet. Der KI-Bericht sagt, diese Bedeutungen seien zu trennen; die verbindliche Benennung ist trotzdem noch nicht festgelegt.
- **Leitstrahl und Räume:** gerichtete Orientierung mit spezialisierten, voneinander abhängigen Arbeitsräumen. Jeder Raum braucht Eingangsabsicht, freies Bearbeiten, Abgleich mit dem inneren Input und einen gesicherten Ausgangsstand.
- **Save State / `Protected_Value`:** Checkpoints schützen gegen eigenmächtige Änderungen durch Agenten/Tools, bleiben für den Nutzer selbst veränderbar.
- **Nutzerhoheit:** KI und Werkzeuge unterstützen oder führen aus; Richtungs-, Änderungs- und Freigabeentscheidungen liegen beim Menschen.
- **Zeitpunkt der Messbarkeit:** frühe Ideenphasen bleiben unbewertet; Messbarkeit und Realitätsprüfung kommen erst nach Sicherung des inneren Inputs.
- **Keine Alles-oder-nichts-Validierung:** einzelne schwache Teile sollen nicht automatisch das gesamte Konzept entwerten.
- **Perfektionsblindheit:** Struktur soll bürokratische Last im Hintergrund auffangen und endlose Prüfschleifen vermeiden; sie darf nicht zum Selbstzweck werden.
- **Drei-Staaten-Modell:** kritisiert sowohl Überregulierung als auch ungeschützte Grenzenlosigkeit und positioniert Ma-FRAME als unterstützende, menschenorientierte Struktur.
- **Leitwert:** Die Existenzberechtigung des Menschen hängt laut ITP nicht von Leistung, Messbarkeit oder kontrollierbarer Produktivität ab.

## Offene Fragen, Lücken und Spannungen

1. **Phasen- und Abschlussbegriffe:** Der KI-Bericht nennt I.1 den aktuellen Abschluss und I.2 als nächsten Schritt; das ITP nennt Abschnitt I „Ideen Entwerfung“. Einheitliche Benennung der Stufen, Zwischenergebnisse und Gates ist nötig.
2. **GUFP und Notation:** Das Akronym belegt zwei verschiedene Rollen. Außerdem verändern sich `x`, `y` und `z` über Formeln hinweg; mathematische Schreibweisen scheinen teilweise Metaphern zu sein.
3. **Validierung und Schutz des Inneren:** Wie wird ein Ergebnis konkret auf `x` zurückgeführt, ohne externe Prüfung oder widersprechende Evidenz zu unterdrücken?
4. **Phase III:** Die sechs Räume sind miteinander gekoppelt, aber Auslöser, Reihenfolge, gemeinsame Bausteine (`PB`), Änderungsrechte und Eintritts-/Austrittsgates sind nicht vollständig definiert. Unklar ist, ob alle Räume für jedes Vorhaben erforderlich sind.
5. **Realisierungsanspruch:** Die Quellen nennen die Phase I.1 eine Live-Validierung, zugleich fehlt laut Autorenbericht eine externe Gegenprobe und ITP ausdrücklich ein Realitätsabgleich. Prozessreflexion ist nicht gleich Wirksamkeitsnachweis.
6. **Quelleninterner Widerspruch:** Der KI-Bericht sagt, Phasen IV–VI seien zunächst leere Platzhalter gewesen, beschreibt im selben Dokument aber spätere Syntheseleistungen; die vorliegende ITP-Fassung enthält Phasen IV–VII bereits. Versions- und Zeitbezug sind nicht ausgewiesen.
7. **Phase V:** Erhebung realer Nutzerdaten wird erwähnt, aber Einwilligung, Datenschutz, Interpretationsregeln und menschliche Freigabe von Optimierungen sind nicht beschrieben.
8. **Phase VI/VII:** Unklar bleibt, ob dies eigene Phasen, dauerhafte Leitregeln oder beides sind und wie sie bei Konflikten mit lokalen Raumregeln wirken.
9. **Anwendungsbereich:** Die angestrebte Universalität von Software, Hardware und Business bis hin zu persönlichen Vorhaben braucht klare Grenzen und optionale Pfade.

Die Punkte werden mit IDs und Bearbeitungsstatus im [Fragen-Backlog](../30_arbeitsstand/OFFENE_FRAGEN.md) geführt.

## Treue zur Quelle und Interpretationsgrenzen

Die XML-Prüfung der drei Quelldateien fand keine Word-Tabellen oder ausgewiesenen Überschriftenstile; das ITP nutzt einen Listenabsatz-Stil. Die Extraktionen bewahren die lesbaren Textinhalte in Dokumentreihenfolge, aber nicht Typografie, Einrückung oder die vollständige visuelle Hierarchie. Zeilenabschließende Leerzeichen werden als Markdown-Formatierung normalisiert. Orthografie, Grammatik, Wiederholungen, wertende Aussagen, Formeln und Metaphern werden nicht redaktionell bereinigt. Die Spezifikation unter `docs/10_framework/` ist dagegen eine strukturierte Synthese: Wo sie über den belegten Wortlaut hinausgeht, markiert sie Ableitungen bzw. `[OFFEN: OF-nnn]`. Keine offene Frage in diesem Entwurf gilt als vom Autor entschieden.

Der Gemini-Deep-Research-Bericht ist eine sekundäre Recherchequelle und kein Beleg für die Wirksamkeit des Frameworks. Seine Analogien können Entwurfsoptionen anregen, entscheiden aber keine offenen Autorfragen. Die im Bericht genannten Kennzahlen und Quellenverweise sind in dieser Repository-Aufarbeitung nicht unabhängig geprüft; vor einer Verwendung als Tatsachenbeleg ist eine separate Quellenprüfung erforderlich.
