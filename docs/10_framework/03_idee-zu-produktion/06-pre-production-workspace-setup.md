# III.6 – Pre-Production & Workspace Setup (Produktionsreife)

- Phase: III – Idee zu Produktion
- Quellen: ITP, Phase III.6

## Zweck

Vor dem harten Übergang in Phase IV die Produktionsumgebung, Werkzeuge, Rollen, Architektur und Tests so vorbereiten, dass die Umsetzung entlang eines freigegebenen Blueprints beginnen kann.

## Abgrenzung

Dies ist die letzte Vorbereitungsstufe; eigentliche Produktion und verbindliche Umsetzung gehören Phase IV. ITP nennt Software, Hardware und gemischte Systeme sowie Sandbox-Tests und integrierte Drittanbieterwerkzeuge.

## Bestandteile

- Simulation/Sandbox: `Test_Sandbox → Concept_Verified`.
- Architektur und Schnittstellen: `Core + Externals_Integrated = System_Blueprint`.
- Workspace-Readiness: `(Tools + Environment) x Roles = Workspace_Ready`.
- Blueprint, Produktionsplan, Brief-Deck, zugewiesene Arbeitsplätze und freigegebene Rollen.
- Fertig-Kriterium: Laborumgebung getestet, Agenten/Rollen eingerichtet und Blueprint vom Operator freigegeben.

## Regeln

- Kritische Architektur-, Belastungs- und Sicherheitsannahmen vor Produktion in isolierter Umgebung testen.
- Drittanbieterwerkzeuge an die eigene Systemlogik anpassen, Abhängigkeiten und Grenzen sichtbar machen.
- Werkzeug- und Rollenentscheidungen vor dem Start der Produktion abschließen.
- Der Übergang in Phase IV ist ein bewusstes menschliches Gate; genaue Kriterien sind noch nicht abschließend beschrieben.

## Beispiel

Vor einem Software-Build werden Integrationen, Rollenrechte und ein isolierter Testablauf geprüft. Erst nach Freigabe des System-Blueprints beginnt die Umsetzung.

## Offene Punkte

- > [OFFEN: OF-005 – Freigabe- und Rückweg-Gate zwischen III.6 und IV bestimmen.]
- > [OFFEN: OF-006 – Verbindliche und optionale Räume sowie Produktionsreife je Vorhabentyp klären.]
- > [OFFEN: OF-011 – Universelle Geltung und Grenzen der Workspace-Vorbereitung konkretisieren.]
- > [OFFEN: OF-014 – Save State und Schutz vor automatischem Überschreiben operationalisieren.]

## Status

Status: Entwurf
