#!/usr/bin/env python3
"""Validate component templates, status values, and open-question references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_SECTIONS = (
    "Zweck",
    "Abgrenzung",
    "Bestandteile",
    "Regeln",
    "Beispiel",
    "Offene Punkte",
    "Status",
)
EXPECTED_PHASES = (
    "01_ideen-entwerfung",
    "02_ideen-entwicklung",
    "03_idee-zu-produktion",
    "04_produktion",
    "05_launch-after-launch",
    "06_execution-regeln",
    "07_systemlogik-philosophie",
)
REQUIRED_FILES = (
    "docs/10_framework/00_ueberblick.md",
    "docs/10_framework/10_prinzipien.md",
    "docs/10_framework/30_glossar.md",
    "docs/20_entscheidungen/0000-template.md",
    "docs/30_arbeitsstand/CHANGELOG.md",
    "docs/30_arbeitsstand/OFFENE_FRAGEN.md",
    "docs/30_arbeitsstand/ROADMAP.md",
    "docs/40_vorlagen/agenten-uebergabe.md",
    "docs/40_vorlagen/baustein.md",
)
VALID_STATUSES = {"Entwurf", "In Arbeit", "Stabil"}
MARKER_START = re.compile(r"\[OFFEN:")
MARKER = re.compile(r"\[OFFEN:\s*(OF-\d{3})\b[^\]]*\]")
STATUS = re.compile(r"^Status:\s*(.*?)\s*$", re.MULTILINE)
BACKLOG_ROW = re.compile(r"^\|\s*(OF-\d{3})\s*\|", re.MULTILINE)
CLOSED_HEADING = "\n## Geschlossene Fragen"
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.DOTALL)
MARKER_SCAN_DIRS = (
    "docs/10_framework",
    "docs/20_entscheidungen",
    "docs/30_arbeitsstand",
)
MARKER_SCAN_FILES = (
    "README.md",
    "docs/00_quellen/QUELLENANALYSE.md",
)


def backlog_ids(content: str) -> tuple[set[str], set[str], list[str]]:
    open_part, _, closed_part = content.partition(CLOSED_HEADING)
    open_ids = BACKLOG_ROW.findall(open_part)
    closed_ids = BACKLOG_ROW.findall(closed_part)
    all_ids = open_ids + closed_ids
    duplicates = sorted(
        question_id
        for question_id in set(all_ids)
        if all_ids.count(question_id) > 1
    )
    return set(open_ids), set(closed_ids), duplicates


def marker_files(root: Path) -> list[Path]:
    files = [
        path
        for directory in MARKER_SCAN_DIRS
        for path in sorted((root / directory).rglob("*.md"))
    ]
    return files + [
        root / relative_path
        for relative_path in MARKER_SCAN_FILES
        if (root / relative_path).is_file()
    ]


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    framework = root / "docs/10_framework"
    components: list[Path] = []
    for phase_name in EXPECTED_PHASES:
        phase = framework / phase_name
        if not phase.is_dir():
            errors.append(f"{phase}: erwarteter Phasenordner fehlt")
            continue
        phase_components = sorted(phase.glob("*.md"))
        if not phase_components:
            errors.append(f"{phase}: keine Markdown-Komponente gefunden")
        components.extend(phase_components)

    expected_phase_paths = {framework / name for name in EXPECTED_PHASES}
    unexpected_phases = sorted(
        phase
        for phase in framework.glob("*")
        if phase.is_dir() and phase not in expected_phase_paths
    )
    for phase in unexpected_phases:
        errors.append(f"{phase}: unerwarteter Phasenordner")

    for relative_path in REQUIRED_FILES:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"{path}: erforderliche Repository-Datei fehlt")

    questions_path = root / "docs/30_arbeitsstand/OFFENE_FRAGEN.md"

    for component in components:
        content = component.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if f"## {section}" not in content.splitlines():
                errors.append(f"{component}: fehlender Abschnitt '## {section}'")

        statuses = STATUS.findall(content)
        if len(statuses) != 1 or statuses[0] not in VALID_STATUSES:
            rendered = ", ".join(repr(status) for status in statuses) or "kein Status"
            errors.append(
                f"{component}: genau ein gültiger Status erforderlich "
                f"({', '.join(sorted(VALID_STATUSES))}; gefunden: {rendered})"
            )

    if questions_path.is_file():
        open_ids, closed_ids, duplicates = backlog_ids(
            questions_path.read_text(encoding="utf-8")
        )
        for question_id in duplicates:
            errors.append(
                f"{questions_path}: {question_id} ist mehrfach eingetragen"
            )

        for path in marker_files(root):
            content = CODE.sub("", path.read_text(encoding="utf-8"))
            markers = MARKER.findall(content)
            if len(MARKER_START.findall(content)) != len(markers):
                errors.append(
                    f"{path}: jeder [OFFEN: ...]-Marker muss geschlossen sein "
                    "und eine OF-nnn-ID enthalten"
                )
            for question_id in sorted(set(markers) - open_ids):
                if question_id in closed_ids:
                    errors.append(
                        f"{path}: {question_id} ist geschlossen; Marker entfernen "
                        "oder Frage wieder öffnen"
                    )
                else:
                    errors.append(
                        f"{path}: {question_id} fehlt in {questions_path}"
                    )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository-Root (für lokale und isolierte Prüfungen)",
    )
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        print("Framework-Prüfung fehlgeschlagen:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Framework-Prüfung erfolgreich.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
