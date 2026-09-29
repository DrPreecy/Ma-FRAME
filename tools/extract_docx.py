#!/usr/bin/env python3
"""Extract the readable body text of DOCX sources to Markdown without dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile
from xml.etree import ElementTree

WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": WORD_NS}
SOURCE_NAMES = {
    "autorenbericht_framework_praxis": "autorenbericht.md",
    "itp": "itp.md",
    "ki_taetigkeitsbericht_framework": "ki-taetigkeitsbericht.md",
}


def element_text(element: ElementTree.Element) -> str:
    parts: list[str] = []
    for child in element.iter():
        if child.tag == f"{{{WORD_NS}}}t":
            parts.append(child.text or "")
        elif child.tag == f"{{{WORD_NS}}}tab":
            parts.append("\t")
        elif child.tag in {f"{{{WORD_NS}}}br", f"{{{WORD_NS}}}cr"}:
            parts.append("\n")
    return "".join(parts)


def body_blocks(document_xml: bytes) -> list[str]:
    root = ElementTree.fromstring(document_xml)
    body = root.find("w:body", NS)
    if body is None:
        raise ValueError("DOCX document has no body")

    blocks: list[str] = []
    for child in body:
        if child.tag == f"{{{WORD_NS}}}p":
            text = element_text(child)
            if text:
                blocks.append(text)
        elif child.tag == f"{{{WORD_NS}}}tbl":
            for row in child.findall("w:tr", NS):
                cells = []
                for cell in row.findall("w:tc", NS):
                    paragraphs = [
                        element_text(paragraph)
                        for paragraph in cell.findall("w:p", NS)
                    ]
                    cells.append("\n".join(paragraphs))
                blocks.append(" | ".join(cells))
    return blocks


def output_name(source: Path) -> str:
    key = re.sub(r"[^a-z0-9]+", "_", source.stem.lower()).strip("_")
    return SOURCE_NAMES.get(key, f"{key}.md")


def extract(source: Path, output_dir: Path) -> Path:
    with ZipFile(source) as archive:
        blocks = body_blocks(archive.read("word/document.xml"))
    output_dir.mkdir(parents=True, exist_ok=True)
    fence_length = max(
        (len(match.group()) for match in re.finditer(r"`+", "\n".join(blocks))),
        default=0,
    ) + 1
    fence = "`" * max(3, fence_length)
    destination = output_dir / output_name(source)
    content = (
        f"# Text-Extraktion: {source.name}\n\n"
        "Die folgende Fassung erhält den lesbaren Text in Dokumentreihenfolge. "
        "Word-Formatierung ist nicht enthalten.\n\n"
        f"{fence}text\n"
        + "\n\n".join(blocks)
        + f"\n{fence}\n"
    )
    destination.write_text(content, encoding="utf-8")
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "sources",
        nargs="*",
        type=Path,
        help="DOCX-Dateien; ohne Angabe werden DOCX-Dateien im Repository-Root verwendet",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("docs/00_quellen"),
        help="Zielverzeichnis für die Markdown-Extraktionen",
    )
    args = parser.parse_args()
    sources = args.sources or sorted(Path(".").glob("*.docx"))
    if not sources:
        parser.error("keine DOCX-Quelldateien gefunden")

    failures = 0
    for source in sources:
        try:
            destination = extract(source, args.output_dir)
            print(f"{source} -> {destination}")
        except (OSError, BadZipFile, KeyError, ElementTree.ParseError, ValueError) as error:
            print(f"Fehler bei {source}: {error}", file=sys.stderr)
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
