from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from tools.check_framework import validate


ROOT = Path(__file__).resolve().parents[1]


class FrameworkStructureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        shutil.copytree(ROOT / "docs", self.root / "docs")

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_repository_structure_is_valid(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_missing_phase_is_reported(self) -> None:
        shutil.rmtree(
            self.root / "docs/10_framework/05_launch-after-launch"
        )

        errors = validate(self.root)

        self.assertTrue(
            any(
                "05_launch-after-launch" in error
                and "erwarteter Phasenordner fehlt" in error
                for error in errors
            )
        )

    def test_empty_phase_is_reported(self) -> None:
        component = self.root / "docs/10_framework/04_produktion/01-produktion.md"
        component.unlink()

        errors = validate(self.root)

        self.assertTrue(
            any(
                "04_produktion" in error
                and "keine Markdown-Komponente" in error
                for error in errors
            )
        )

    def test_unexpected_phase_is_reported(self) -> None:
        unexpected = self.root / "docs/10_framework/08_unbekannt"
        unexpected.mkdir()
        (unexpected / "01-baustein.md").write_text("# Test\n", encoding="utf-8")

        errors = validate(self.root)

        self.assertTrue(
            any(
                "08_unbekannt" in error
                and "unerwarteter Phasenordner" in error
                for error in errors
            )
        )

    def test_all_structural_errors_are_reported_together(self) -> None:
        shutil.rmtree(self.root / "docs/10_framework/07_systemlogik-philosophie")
        (self.root / "docs/30_arbeitsstand/OFFENE_FRAGEN.md").unlink()
        (self.root / "docs/40_vorlagen/agenten-uebergabe.md").unlink()

        errors = validate(self.root)

        self.assertTrue(any("07_systemlogik-philosophie" in error for error in errors))
        self.assertTrue(any("OFFENE_FRAGEN.md" in error for error in errors))
        self.assertTrue(any("agenten-uebergabe.md" in error for error in errors))

    def test_existing_component_rules_still_apply(self) -> None:
        component = (
            self.root
            / "docs/10_framework/04_produktion/01-produktion.md"
        )
        component.write_text(
            component.read_text(encoding="utf-8").replace("## Zweck", "## Ziel"),
            encoding="utf-8",
        )

        errors = validate(self.root)

        self.assertTrue(any("fehlender Abschnitt '## Zweck'" in error for error in errors))

    def test_marker_outside_phase_must_reference_backlog_row(self) -> None:
        overview = self.root / "docs/10_framework/00_ueberblick.md"
        overview.write_text(
            overview.read_text(encoding="utf-8") + "\n[OFFEN: OF-999]\n",
            encoding="utf-8",
        )
        backlog = self.root / "docs/30_arbeitsstand/OFFENE_FRAGEN.md"
        backlog.write_text(
            backlog.read_text(encoding="utf-8") + "\nOF-999 nur im Fließtext.\n",
            encoding="utf-8",
        )

        errors = validate(self.root)

        self.assertTrue(any("OF-999 fehlt" in error for error in errors))

    def test_marker_must_not_reference_closed_question(self) -> None:
        overview = self.root / "docs/10_framework/00_ueberblick.md"
        overview.write_text(
            overview.read_text(encoding="utf-8") + "\n[OFFEN: OF-999]\n",
            encoding="utf-8",
        )
        backlog = self.root / "docs/30_arbeitsstand/OFFENE_FRAGEN.md"
        backlog.write_text(
            backlog.read_text(encoding="utf-8")
            + "\n| OF-999 | Erledigt | I | Geschlossen | Ergebnis |\n",
            encoding="utf-8",
        )

        errors = validate(self.root)

        self.assertTrue(any("OF-999 ist geschlossen" in error for error in errors))

    def test_duplicate_backlog_id_is_reported(self) -> None:
        backlog = self.root / "docs/30_arbeitsstand/OFFENE_FRAGEN.md"
        content = backlog.read_text(encoding="utf-8")
        backlog.write_text(
            content.replace(
                "\n## Geschlossene Fragen",
                "\n| OF-001 | Duplikat | I | Offen | Prüfen |\n"
                "\n## Geschlossene Fragen",
            ),
            encoding="utf-8",
        )

        errors = validate(self.root)

        self.assertTrue(any("OF-001 ist mehrfach eingetragen" in error for error in errors))

    def test_marker_example_in_code_is_ignored(self) -> None:
        overview = self.root / "docs/10_framework/00_ueberblick.md"
        overview.write_text(
            overview.read_text(encoding="utf-8") + "\n`[OFFEN: OF-999]`\n",
            encoding="utf-8",
        )

        self.assertEqual(validate(self.root), [])


if __name__ == "__main__":
    unittest.main()
