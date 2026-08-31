# User-Facing Only

[English](README.md) | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/Ljhhhhhh/user-facing-only-skill?style=flat-square)](https://github.com/Ljhhhhhh/user-facing-only-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-111827?style=flat-square)](https://agentskills.io)

**Keep AI build instructions, developer scaffolding, and correction history out of finished deliverables.**

When generating UI prototypes, code, or reports, AI models frequently leak prompt context into the final output:

- **Development notes become UI copy:** A prompt specifying *"use mock data for now"* renders a prominent banner: *“⚠️ Notice: Using mock data. Connect real backend before production.”*
- **Change requests become artifact titles:** A prompt asking to *"remove the export button"* produces the heading: *“Dashboard v2 (Export button removed)”*.
- **Internal drafting constraints leak to clients:** A prompt requesting a *"polite status update"* begins with: *“As instructed, this report has been written in a polite tone...”*

**User-Facing Only** enforces a strict boundary between builder instructions and user-facing artifacts: **prompts guide construction, while deliverables serve the end user**. Temporary scaffolding, conversational reasoning, and discarded iterations are kept out of the final result.

## Quick start

Ask Codex to install the skill:

```text
Use $skill-installer to install user-facing-only from https://github.com/Ljhhhhhh/user-facing-only-skill/tree/main/skills/user-facing-only
```

Restart Codex after installation, then work normally. Automatic discovery is limited to requests with a real user-facing leakage risk, such as demo or mock instructions, presenter guidance, internal rationale, temporary shortcuts, corrected requirements, or an explicit leakage review.

You can also invoke it explicitly:

```text
Use $user-facing-only to review this prototype before handoff. Keep implementation constraints and presenter guidance out of the user-facing result.
```

## Automatic routing boundary

Implicit invocation remains enabled for deliverables at real risk of exposing construction context or superseded requirements. Ordinary implementation work does not need this skill merely because it creates code, UI, APIs, scripts, or documentation.

Explicit `$user-facing-only` invocation always remains available. Review-only requests produce findings without modifying the artifact.

## The failure mode

AI agents often treat every sentence in a request as candidate product content. This creates four recurring defects:

- **Instruction leakage:** implementation constraints become headings, cards, help text, or report copy.
- **Unauthorized additions:** unrequested ideas are silently implemented just because they seemed neat.
- **Wrong-surface content:** presenter notes, design rationale, or acceptance criteria appear in the product itself.
- **Correction residue:** rejected ideas survive as “v2,” “removed,” negative rules, fixtures, or explanatory copy.

User-Facing Only addresses the decision error before copy is written.

## Before and after

| Request context | Leaked artifact (Incorrect) | Clean deliverable (Correct) |
|---|---|---|
| “Build a checkout page using mock data for now.” | Banner: *“⚠️ Notice: Using mock data. Connect real gateway before production.”* | Clean checkout flow with no internal data-source notes exposed to the user. |
| “Reuse the existing User model for this profile page.” | Subheading: *“User Profile built on the existing User model.”* | Architecture constraint guides implementation only; omitted from user-facing copy. |
| “Remove the auto-approval toggle from the admin panel.” | Heading: *“Admin Panel v2 — Auto-approval removed.”* | Clean manual-review interface containing only active workflows with no correction traces. |
| “Draft a project update emphasizing on-time delivery.” | Opening line: *“Note: As requested, this summary highlights on-time delivery.”* | Professional update delivered directly without exposing prompt instructions or metadata. |

## How it works

```text
User Request / Correction
    ↓
Identify the latest authorized artifact, audience, and task
    ↓
Build or review only that target
    ↓
Inspect the result as a user who never saw the conversation
    ↓
Deliver Pure Artifact
```

The skill follows one principle:

> The finished artifact contains only what its intended audience needs from the latest authorized requirements. Construction context guides implementation but does not become artifact content.

Corrections replace superseded product state. Required disclosures and legitimate history remain when the audience needs them. Review-only work reports findings without editing files.

See [`SKILL.md`](skills/user-facing-only/SKILL.md) for the complete operating rules and cases.

## Good use cases

- interfaces and HTML prototypes;
- demo systems with presenter guidance or prepared fixtures;
- reports, decks, and exports;
- CLI output and user-facing documentation;
- deliverables built from long or frequently corrected conversations;
- reviews for prompt structure, design rationale, or internal terminology leaking into the result.

## What this skill does not do

User-Facing Only is deliberately narrow. It does not:

- act as a general UX-writing or accessibility audit;
- decide API compatibility, migration, or versioning policy;
- require provenance or sample-data labels by default;
- require tests, comments, compatibility mechanisms, or legitimate historical records to be deleted;
- decide artifact meaning from fixed words or mechanical content scans;
- create presenter notes or technical documentation unless those artifacts are in scope;
- replace domain-specific safety, legal, or product requirements.

## Manual installation

Clone the repository into a stable source directory and link the skill into Codex:

```bash
mkdir -p ~/.codex/skill-sources ~/.codex/skills
git clone https://github.com/Ljhhhhhh/user-facing-only-skill.git ~/.codex/skill-sources/user-facing-only-skill
ln -s ~/.codex/skill-sources/user-facing-only-skill/skills/user-facing-only ~/.codex/skills/user-facing-only
```

To update an existing clone:

```bash
git -C ~/.codex/skill-sources/user-facing-only-skill pull --ff-only
```

Agents that discover the shared Agent Skills directory can link the same source:

```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/skill-sources/user-facing-only-skill/skills/user-facing-only ~/.agents/skills/user-facing-only
```

Do not create the link over an existing skill directory. Inspect or move the existing installation first.

## Repository structure

```text
.
├── .github/workflows/
│   └── validate.yml
├── evals/
│   └── cases.md
├── scripts/
│   └── validate.py
├── skills/
│   └── user-facing-only/
│       ├── SKILL.md
│       └── agents/
│           └── openai.yaml
├── LICENSE
├── README.md
└── README.zh-CN.md
```

The installed skill has no runtime dependencies, network calls, or bundled executables. Repository validation uses Python and PyYAML in CI; those development checks are not part of skill execution.

## Contributing

Issues and pull requests are welcome. The most useful contributions are minimal reproducible examples of boundary failures:

- the user request;
- the incorrect user-facing result;
- the expected current-state artifact;
- why the example generalizes beyond one product or noun.

Keep the behavioral suite small and orthogonal in `evals/cases.md`. Deterministic CI validates package structure only; behavioral claims require fresh-context execution of the cases.

Avoid adding keyword blacklists, taxonomies, or universal rules based on a single failure. Prefer the smallest change that improves the audience-and-authorization decision.

## License

[MIT](LICENSE)
