---
name: artifact-boundary
description: Prevent unrequested scope and process residue in finished artifacts and implementations. Use for interfaces, prototypes, demo systems, reports, decks, exports, CLI text, application code, APIs, schemas, or refactors where rationale, rejected ideas, or legacy compatibility could leak into the result.
---

# Artifact Boundary

Build the current authorized end state, not the conversation or legacy states that preceded it.

## Core rules

1. **Implement only authorized scope.** Include what the user requested and what is strictly necessary for it to work. Propose optional improvements separately; do not silently add them.
2. **Requirements are not page copy.** Constraints, rationale, demo notes, implementation details, internal codes, and agent reasoning stay out of the artifact unless the user explicitly asks to expose them or an affected user needs a truthful disclosure.
3. **A correction replaces the target.** Recompute the deliverable from the latest valid direction instead of appending a correction story.
4. **Rejected content disappears.** Delete it and every residual reference from the current product and deliverables. Do not leave names, placeholders, comments, fixtures, tests, headings, version labels, negative rules, or “removed/without” notices.
5. **Compatibility requires authorization.** Do not add legacy branches, shims, aliases, adapters, fallback formats, dual-write paths, deprecated APIs, or version switches unless the user explicitly requires compatibility. If current consumers may depend on the old behavior, surface the impact instead of silently preserving it.
6. **Presentation changes framing, not truth.** Demo navigation, fixtures, and layout may differ; business meaning, permissions, status, and limitations may not.
7. **History is exceptional.** Retain superseded decisions only when the requested artifact is itself history-bearing—such as a retrospective, audit record, decision log, migration history, or regulated record—and confine that history to it.

## Workflow

### 1. Define the boundary

Before editing, identify:

- the finished artifact;
- its real audience and task;
- the latest authorized target;
- any disclosure required for safety, law, data provenance, or honest operation.

If an addition cannot be traced to the target or strict necessity, leave it out.

### 2. Classify candidate content

For every proposed element, decide whether it is:

- **User-facing:** needed by the audience to understand or operate the artifact;
- **Behavior:** implemented in the product, not narrated as copy;
- **Internal:** belongs in code, tests, presenter notes, or technical documentation only when those are in scope;
- **Compatibility:** implement only when explicitly requested; otherwise report known breakage risk and keep the current path singular;
- **Rejected:** delete completely from the current artifact.

Placement does not create authorization. “Put it in documentation” is not a reason to create unrequested documentation.

### 3. Build from the target state

Write in the audience’s language. Use business concepts instead of implementation vocabulary, and show only information that helps the next valid action.

When the user corrects scope, remove the rejected branch first, then rebuild the affected area from the corrected target. Do not preserve the correction as a feature, title, explanation, or lesson inside the deliverable.

### 4. Review as a fresh user

Inspect the rendered or executed result without relying on the conversation. Ask:

- Does every visible element serve the audience’s task?
- Can any sentence be understood only by knowing how the artifact was built?
- Did a rejected idea survive indirectly?
- Would normal, demo, and exported views make the same factual claims?

Fix the artifact when implementation was requested. For review-only work, report the findings without changing it.

## Cases

| Situation | Correct result | Incorrect result |
|---|---|---|
| A bathroom was requested; an unrequested swimming pool was added and then rejected. | Deliver only the bathroom. Delete the pool and all references to it. Generalize the learning privately as “do not implement unrequested scope.” | “Bathroom v2 (pool removed),” a “no swimming pools” rule, a changelog entry, leftover component names, fixtures, or tests. |
| A demo system is designed around a seven-minute presentation path and a convenient OCR shortcut. | The interface shows the real business task, states, and actions. Put timing in presenter notes and the shortcut in technical material only if those artifacts were requested. Disclose sample data once if needed for honesty. | Cards titled “7-minute demo path,” “why this case is suitable,” or product-building principles presented as business content. |
| A ticket feature must reuse the current data model. | Implement the ticket workflow within that constraint. Keep the constraint in code or an authorized technical document. | A user-facing heading such as “Modern ticket handling on the current data model,” or extra workflows added to demonstrate architecture. |
| An API is replaced by a new contract, and compatibility was not requested. | Migrate in-scope callers to the new contract and remove the old path. If unknown or external consumers may exist, report that risk before making a breaking decision. | Keeping both endpoints, adding a version switch, accepting both payload shapes, or labeling code “temporary compatibility” without authorization. |
| The user explicitly requests a retrospective of a rejected migration approach. | Explain the rejected approach and decision in the retrospective only. The current product remains free of it. | Suppressing relevant history from the retrospective, or copying that history into the product UI and current operating guide. |

Examples illustrate the rules; their nouns are not new universal rules.

## Handoff gate

Do not hand off until all applicable checks pass:

- **Scope:** every addition is requested or strictly necessary.
- **Clean state:** rejected names, labels, comments, fixtures, tests, and version markers are absent.
- **Single current path:** no compatibility branch exists without explicit authorization.
- **Artifact-only:** the result makes sense without the conversation.
- **Truth:** demo, normal, and export surfaces do not contradict one another.
- **Rendered behavior:** relevant visible and interactive states were actually inspected.
