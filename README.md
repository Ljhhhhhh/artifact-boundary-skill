# Artifact Boundary

[English](README.md) | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/Ljhhhhhh/artifact-boundary-skill?style=flat-square)](https://github.com/Ljhhhhhh/artifact-boundary-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-111827?style=flat-square)](https://agentskills.io)

**Keep AI build instructions, developer scaffolding, and correction history out of finished deliverables.**

When generating UI prototypes, code, or reports, AI models frequently leak prompt context into the final output:

- **Development notes become UI copy:** A prompt specifying *"use mock data for now"* renders a prominent banner: *“⚠️ Notice: Using mock data. Connect real backend before production.”*
- **Change requests become artifact titles:** A prompt asking to *"remove the export button"* produces the heading: *“Dashboard v2 (Export button removed)”*.
- **Internal drafting constraints leak to clients:** A prompt requesting a *"polite status update"* begins with: *“As instructed, this report has been written in a polite tone...”*

**Artifact Boundary** enforces a strict boundary between builder instructions and user-facing artifacts: **prompts guide construction, while deliverables serve the end user**. Temporary scaffolding, conversational reasoning, and discarded iterations are kept out of the final result.

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

- **Instruction leakage:** implementation constraints become headings, cards, help text, or report copy.
- **Unauthorized additions:** unrequested ideas are silently implemented just because they seemed neat.
- **Wrong-surface content:** presenter notes, design rationale, or acceptance criteria appear in the product itself.
- **Correction residue:** rejected ideas survive as “v2,” “removed,” negative rules, fixtures, or explanatory copy.

Artifact Boundary addresses the decision error before copy is written.

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
Two-Pass Decoupling (Quarantine control context from target spec)
    ↓
Pure Implementation (Build authorized domain artifact only)
    ↓
Pre-Handoff Static Scan (Regex scan for boundary leaks)
    ↓
Fresh User Blind Test Gate
    ↓
Deliver Pure Artifact
```

The skill applies five core decisions:

1. **Two-Pass Decoupling** — isolate prompt control context (timings, defenses, mock notes) from target business specifications.
2. **Fresh User Blind Test** — every visible element must make complete sense to a user who never saw the prompt.
3. **Surgical Cutover** — rebuild from current target as if superseded features never existed, with zero negative rules or version tags.
4. **Behavior as Behavior** — implement constraints as code logic rather than explanatory on-screen prose.
5. **No Structural Meta-Scaffolding** — eliminate delivery explanation bars, prompt-defense banners, and developer wrappers.

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
├── README.md
└── README.zh-CN.md
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
