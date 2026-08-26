# Artifact Boundary

[![Release](https://img.shields.io/github/v/release/Ljhhhhhh/artifact-boundary-skill?style=flat-square)](https://github.com/Ljhhhhhh/artifact-boundary-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-111827?style=flat-square)](https://agentskills.io)

**Stop AI build instructions, demo scaffolding, and correction history from leaking into the finished product.**

You ask an agent to build a business app *for a seven-minute demo*. It ships cards titled **“Seven-minute demo path”** and **“Why this case is suitable.”** You ask it to remove an unrequested feature. It ships **“v2 — feature removed.”**

Artifact Boundary teaches the agent to compile the conversation into the current authorized target before it builds. The prompt guides the work; it does not become the artifact.

## Quick start

Ask Codex to install the skill:

```text
Use $skill-installer to install artifact-boundary from https://github.com/Ljhhhhhh/artifact-boundary-skill/tree/main/skills/artifact-boundary
```

Restart Codex after installation, then work normally. The skill supports automatic discovery when a request contains implementation constraints, demo guidance, internal reasoning, or corrected requirements.

You can also invoke it explicitly:

```text
Use $artifact-boundary to review this prototype before handoff. Keep implementation constraints and presenter guidance out of the user-facing result.
```

## The failure mode

AI agents often treat every sentence in a request as candidate product content. This creates four recurring defects:

- **Instruction-to-artifact leakage:** implementation constraints become headings, cards, help text, or report copy.
- **Unauthorized promotion:** an optional idea is silently implemented because it seems useful or impressive.
- **Wrong-surface content:** presenter notes, design rationale, or acceptance criteria appear in the product itself.
- **Correction residue:** rejected ideas survive as “v2,” “removed,” negative rules, fixtures, or explanatory copy.

Artifact Boundary addresses the decision error before copy is written.

## Before and after

| Request context | Leaky artifact | Boundary-safe result |
|---|---|---|
| “Build this system for a seven-minute presentation.” | A dashboard card named “Seven-minute demo path.” | The product shows the business task. Timing stays out unless presenter material was requested. |
| “Reuse the current data model.” | A headline saying “Modern workflows on the current data model.” | The constraint shapes implementation; it is not narrated to the product user. |
| “Remove the auto-approval feature.” | “Manual review v2 — auto-approval removed.” | The current product contains the manual-review workflow, with no correction story. |
| “Use sample data.” | Automatic provenance labels and build notes. | No visible attribution unless requested or omission would be unsafe, unlawful, or materially misleading. |

## How it works

```text
conversation
    ↓
compile the current authorized target
    ↓
authorize scope
    ↓
qualify user-facing content
    ↓
route behavior and internal material correctly
    ↓
build and review as a fresh user
```

The skill applies five core decisions:

1. **Compile the current target** — identify the artifact, audience, task, authorized behavior, and genuinely required disclosures.
2. **Authorize scope before implementation** — propose optional ideas instead of silently shipping them.
3. **Qualify user-facing content** — visible content must serve the intended user's task or a required disclosure.
4. **Route content to the correct surface** — implement behavior as behavior; keep internal and presenter material outside the product unless those artifacts were requested.
5. **Replace corrected state** — rebuild from the latest target instead of narrating the correction.

See [`SKILL.md`](skills/artifact-boundary/SKILL.md) for the complete operating rules and cases.

## Good use cases

- interfaces and HTML prototypes;
- demo systems with presenter guidance or prepared fixtures;
- reports, decks, and exports;
- CLI output and user-facing documentation;
- deliverables built from long or frequently corrected conversations;
- reviews for prompt structure, design rationale, or internal terminology leaking into the result.

## What this skill does not do

Artifact Boundary is deliberately narrow. It does not:

- act as a general UX-writing or accessibility audit;
- decide API compatibility, migration, or versioning policy;
- require provenance or sample-data labels by default;
- require tests, comments, compatibility mechanisms, or legitimate historical records to be deleted;
- create presenter notes or technical documentation unless those artifacts are in scope;
- replace domain-specific safety, legal, or product requirements.

## Manual installation

Clone the repository into a stable source directory and link the skill into Codex:

```bash
mkdir -p ~/.codex/skill-sources ~/.codex/skills
git clone https://github.com/Ljhhhhhh/artifact-boundary-skill.git ~/.codex/skill-sources/artifact-boundary-skill
ln -s ~/.codex/skill-sources/artifact-boundary-skill/skills/artifact-boundary ~/.codex/skills/artifact-boundary
```

To update an existing clone:

```bash
git -C ~/.codex/skill-sources/artifact-boundary-skill pull --ff-only
```

Agents that discover the shared Agent Skills directory can link the same source:

```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/skill-sources/artifact-boundary-skill/skills/artifact-boundary ~/.agents/skills/artifact-boundary
```

Do not create the link over an existing skill directory. Inspect or move the existing installation first.

## Repository structure

```text
.
├── skills/
│   └── artifact-boundary/
│       ├── SKILL.md
│       └── agents/
│           └── openai.yaml
├── LICENSE
└── README.md
```

The skill has no runtime dependencies, network calls, scripts, or bundled executables.

## Contributing

Issues and pull requests are welcome. The most useful contributions are minimal reproducible examples of boundary failures:

- the user request;
- the incorrect user-facing result;
- the expected current-state artifact;
- why the example generalizes beyond one product or noun.

Avoid adding keyword blacklists or universal rules based on a single failure. Changes should improve the underlying audience, authorization, content-qualification, or surface-routing decision.

## License

[MIT](LICENSE)
