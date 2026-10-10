#!/usr/bin/env python3
"""Dependency-free structural check for the language-agnostic project starter."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "PROJECT.md",
    "AGENTS.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/workflows/template-validation.yml",
)

def main() -> int:
    errors: list[str] = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing: {name}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty: {name}")

    for name, expected in {
        "PROJECT.md": ("Sources of truth", "Authorization"),
        "AGENTS.md": ("Validation", "Git & delivery"),
    }.items():
        file_path = ROOT / name
        if not file_path.is_file():
            continue
        text = file_path.read_text(encoding="utf-8").casefold()
        for section in expected:
            if section.casefold() not in text:
                errors.append(f"{name}: missing section {section}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Project template structural checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
