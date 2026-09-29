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
VALID_STATUSES = {"Entwurf", "In Arbeit", "Stabil"}
MARKER_START = re.compile(r"\[OFFEN:")
MARKER = re.compile(r"\[OFFEN:\s*(OF-\d{3})\b[^\]]*\]")
QUESTION_ID = re.compile(r"\bOF-\d{3}\b")
STATUS = re.compile(r"^Status:\s*(.*?)\s*$", re.MULTILINE)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    framework = root / "docs/10_framework"
    components = sorted(
        path
        for phase in framework.glob("[0-9][0-9]_*")
        if phase.is_dir()
        for path in phase.glob("*.md")
    )
    if not components:
        return [f"{framework}: keine Komponenten in den Phasenordnern gefunden"]

    questions_path = root / "docs/30_arbeitsstand/OFFENE_FRAGEN.md"
    if not questions_path.is_file():
        return [f"{questions_path}: Fragen-Backlog fehlt"]
    question_ids = set(QUESTION_ID.findall(questions_path.read_text(encoding="utf-8")))

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

        markers = MARKER.findall(content)
        if len(MARKER_START.findall(content)) != len(markers):
            errors.append(
                f"{component}: jeder [OFFEN: ...]-Marker muss geschlossen sein "
                "und eine OF-nnn-ID enthalten"
            )
        for question_id in sorted(set(markers) - question_ids):
            errors.append(
                f"{component}: {question_id} fehlt in {questions_path}"
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
