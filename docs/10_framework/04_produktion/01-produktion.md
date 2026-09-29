# IV – Produktion

- Phase: IV – Produktion
- Quellen: ITP, Phase IV; KI-Tätigkeitsbericht, Abschnitte 3 und 5

## Zweck

Den in Phase III freigegebenen Blueprint durch Orchestrierung vorhandener Werkzeuge und menschlicher/agentischer Rollen in ein gebautes Produkt überführen.

## Abgrenzung

Produktion erfindet laut ITP weder ein neues Code-System noch eine Programmiersprache oder neuartige Agentensoftware. Sie ist der harte Schnitt von reversibler Vorbereitung zu verbindlicher Umsetzung; konzeptionelle Grundsatzdiskussionen gehören nicht in den Produktionsraum.

## Bestandteile

- Freigegebene `Blueprint_Spec`.
- Ausführungsauftrag, Rollen und abgegrenzter Spielraum für Agenten.
- Modulare Arbeits-, Test- und Zusammenführungsabläufe.
- `Output_Build`; Soll-Ist-Vergleich `Blueprint_Spec == Output_Build`.

## Regeln

- Nur innerhalb der zugewiesenen Grenzen arbeiten.
- Pläne nicht ohne explizite Freigabe des Operators verwerfen.
- Abweichungen vom Blueprint sichtbar machen und zur menschlichen Entscheidung eskalieren.
- Fertig ist die Umsetzung, wenn der gebaute Zustand nachweisbar der Spezifikation entspricht.

## Beispiel

Ein Agent implementiert ein freigegebenes Modul, führt vorgesehene Tests aus und meldet eine nicht spezifizierte Abhängigkeit, statt eigenmächtig den Architekturplan zu ändern.

## Offene Punkte

- > [OFFEN: OF-005 – Produktionsstart, Abweichungsfreigabe und Rückkehr in die Planung definieren.]
- > [OFFEN: OF-014 – Schutz und Wiederherstellung des freigegebenen Produktionsstands klären.]

## Status

Status: Entwurf
