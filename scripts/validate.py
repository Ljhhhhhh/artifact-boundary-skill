#!/usr/bin/env python3
"""Validate package structure without claiming behavioral correctness."""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "user-facing-only" / "SKILL.md"
OPENAI = ROOT / "skills" / "user-facing-only" / "agents" / "openai.yaml"
CASES = ROOT / "evals" / "cases.md"


def main() -> None:
    content = SKILL.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) != 3:
        raise SystemExit("SKILL.md has invalid frontmatter")
    frontmatter = yaml.safe_load(parts[1])
    if frontmatter.get("name") != "user-facing-only" or not frontmatter.get("description"):
        raise SystemExit("SKILL.md requires its name and description")

    metadata = yaml.safe_load(OPENAI.read_text(encoding="utf-8"))
    interface = metadata.get("interface", {})
    if "$user-facing-only" not in interface.get("default_prompt", ""):
        raise SystemExit("default_prompt must mention $user-facing-only")
    if metadata.get("policy", {}).get("allow_implicit_invocation") is not True:
        raise SystemExit("implicit invocation must remain enabled")

    cases = CASES.read_text(encoding="utf-8")
    if sum(line.startswith("## Case ") for line in cases.splitlines()) != 4:
        raise SystemExit("evals/cases.md must contain four behavioral cases")

    print("Package structure validation passed")


if __name__ == "__main__":
    main()
